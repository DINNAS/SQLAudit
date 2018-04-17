# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from common.mymako import render_mako_context


def dashboard(request):
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

    BK_PAAS_HOST = "http://paas.dianjoy.com"
    url = "http://{host}/api/c/compapi/cc/get_app_host_list/".format(host=BK_PAAS_HOST)

    try:
        http_get = requests.get(url=url, params=params)
        if http_get.status_code == 200:
            if http_get['code'] == '00':
                print http_get
                host_list = http_get['data']
                host_sum = len(host_list)
                return host_sum
            else:
                logger.error(http_get)
                sys.exit(2)
        else:
            logger.error(http_get.text)
            sys.exit(3)
    except Exception:
        logger.error(traceback.format_exc())
        sys.exit(4)

    if host_sum:
        host_count = {'host_inv': host_sum}

    return render_mako_context(request, '/home_application/dashboard.html', host_count)


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')
