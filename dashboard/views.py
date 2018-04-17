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
    #params
    app_code = settings.APP_ID
    app_secret = settings.APP_TOKEN
    username = 'admin'
    app_id = '2'

    params = {
        'app_code': app_code,
        'app_secret': app_secret,
        'username': username,
        'app_id': app_id
    }

    BK_PAAS_HOST = "http://paas.dianjoy.com:80"
    url = "http://{host}/api/c/compapi/cc/get_app_host_list/".format(host=BK_PAAS_HOST)

    # try:
    #     http_get = requests.get(url=url, params=params)
    #     if http_get.status_code == 200:
    #         if http_get['code'] == '00':
    #             print http_get
    #             host_list = http_get['data']
    #             host_sum = len(host_list)
    #             return host_sum
    #         else:
    #             logger.error(http_get)
    #             sys.exit(2)
    #     else:
    #         logger.error(http_get.text)
    #         sys.exit(3)
    # except Exception:
    #     logger.error(traceback.format_exc())
    #     sys.exit(4)

    # if host_sum:
    #     host_count = {'host_inv': host_sum}
    host_count = {'host_inv': 432}

    return render_mako_context(request, '/dashboard/dashboard.html', host_count)

