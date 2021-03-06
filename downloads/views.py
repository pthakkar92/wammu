from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from downloads.models import Download, Release, get_program, get_latest_releases, get_current_downloads, PLATFORM_CHOICES, PROGRAM_CHOICES
from django.http import Http404, HttpResponse


def list(request, program, platform):
    if not program in [x[0] for x in PROGRAM_CHOICES]:
        raise Http404('No such program %s.' % program)
    if not platform in [x[0] for x in PLATFORM_CHOICES]:
        raise Http404('No such platform %s.' % platform)

    if platform == 'win32':
        return redirect('downloads.views.list', program=program, platform='source')

    downloads = get_current_downloads(program, platform)

    stable_release, stable_downloads = downloads[0]
    try:
        testing_release, testing_downloads = downloads[1]
    except IndexError:
        testing_release, testing_downloads = (None, None)

    if stable_downloads.count() == 0:
        raise Http404('No such download option %s/%s.' % (program, platform))

    for c in PLATFORM_CHOICES:
        if platform == c[0]:
            platform_name = c[1]

    result = render_to_response('downloads/list.html', RequestContext(request, {
        'stable_release': stable_release,
        'testing_release': testing_release,
        'stable_downloads': stable_downloads,
        'testing_downloads': testing_downloads,
        'program_include': 'downloads/programs/%s-%s.html' % (program, platform),
        'program': get_program(program),
        'program_name': program,
        'platform': platform_name,
    }))
    return result

def release(request, program,  version):

    release = get_object_or_404(Release, program = program, version = version)
    downloads = Download.objects.filter(release = release).order_by('location')

    if downloads.count() == 0:
        raise Http404('No such download option %s/%s.' % (program, version))

    result = render_to_response('downloads/release.html', RequestContext(request, {
        'release': release,
        'downloads': downloads,
        'program': get_program(program),
        'program_name': program,
    }))
    return result


def program(request, program):
    if not program in [x[0] for x in PROGRAM_CHOICES]:
        raise Http404('No such program %s.' % program)
    if program in ['python-gammu']:
        raise Http404('No such program %s.' % program)

    stable_release, testing_release = get_latest_releases(program)

    downloads = get_current_downloads(program, 'source')

    return render_to_response('downloads/program.html', RequestContext(request, {
        'stable_release': stable_release,
        'testing_release': testing_release,
        'platforms': PLATFORM_CHOICES[:1],
        'downloads': downloads,
        'program': get_program(program),
        'program_name': program,
    }))

def download(request):
    downloads = get_current_downloads('gammu', 'source')
    downloads += get_current_downloads('wammu', 'source')

    return render_to_response('downloads/index.html', RequestContext(request, {
        'downloads': downloads,
        'platforms': PLATFORM_CHOICES[:1],
    }))

def doap(request, program):
    if not program in [x[0] for x in PROGRAM_CHOICES]:
        raise Http404('No such program %s.' % program)

    downloads = get_current_downloads(program, None)

    return render_to_response('downloads/doap/%s.xml' % program, RequestContext(request, {
        'downloads': downloads[0][1],
        'release': downloads[0][0],
    }), content_type = 'application/xml')

def pad(request, program):
    if not program in [x[0] for x in PROGRAM_CHOICES]:
        raise Http404('No such program %s.' % program)

    downloads = get_current_downloads(program, 'source')

    release = downloads[0][0]
    download = downloads[0][1].filter(location__iendswith='.zip')[0]

    return render_to_response('downloads/pad/%s.xml' % program, RequestContext(request, {
        'download': download,
        'release': release,
    }), content_type = 'application/xml')

def padmap(request):
    '''
    Public list of PAD files.
    '''
    response = HttpResponse(content_type='text/plain')
    response.write('http://wammu.eu/api/pad/gammu.xml\n')
    response.write('http://wammu.eu/api/pad/wammu.xml\n')
    return response
