# -*- coding: utf-8 -*-

from common.mymako import render_mako_context
# Create your views here.
import requests
import traceback
import logging
import sys

from django.conf import settings
# 公共URL配置

# set the logger
FORMAT = '[%(asctime)s %(filename)s(line:%(lineno)d) %(levelname)s] %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('log')
logger.setLevel(logging.DEBUG)



def home(request):
    """
    首页
    """
    VERSION = "v3.0.6"
    BK_PAAS_HOST = "http://paas.dianjoy.com:80"
    url = "http://{host}/api/c/compapi/hosts/search".format(host=BK_PAAS_HOST, version=VERSION)
    headers = {
    }
    params = {
        "ip":{
            "data":[

            ],
            "exact":1,
            "flag":"bk_host_innerip|bk_host_outerip"
        },

        "page":{
            "start":0,
            "limit":10,
            "sort":"bk_host_name"
        },
        "pattern":""
        }

    try:
        http_post = requests.post(url=url, params=params, headers=headers)
        print http_post.status_code
        if http_post.status_code == 200:
            if http_post['bk_error_code'] == 0:
                host_set_num = http_post['data']['count']
                return host_set_num
            else:
                logger.error(http_post)
                sys.exit(2)
        else:
            logger.error(http_post.text)
            sys.exit(3)
    except Exception:
        logger.error(traceback.format_exc())
        sys.exit(4)

    if host_set_num:
        host_count = {'host_inv': host_set_num}

    return render_mako_context(request, '/dashboard/dashboard.html', host_count)

