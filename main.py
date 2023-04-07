import credentials.loging_to_gs as lgs
import modules.get_audit_urls as gu
import modules.request_tests as rt
import modules.update_velocidad as ud
import modules.update_cache as uc
import modules.update_code_ratio as ucr
import modules.update_web_vitals as uwv
import modules.update_pagespeedinsights as psi
import modules.update_mobile_friendly_test as mft

lgs.log_to_gs()

mobile_results = rt.request_tests_mobile(gu.urls_list)
desktop_results = rt.request_tests_desktop(gu.urls_list)

# ALL TEST
<<<<<<< HEAD
=======
# ALL TEST
>>>>>>> cc12a95c7e1e4a336a9403adfdcb79397b0987ed
ud.update_velocidad_mobile(mobile_results, gu.wks_velocidad)
ud.update_velocidad_desktop(desktop_results, gu.wks_velocidad)
ucr.update_code_ratio(mobile_results, gu.wks_velocidad)

uc.update_cache(mobile_results, gu.wks_cache)

uwv.update_web_vitals_mobile(mobile_results, gu.wks_webVitals)
uwv.update_web_vitals_desktop(desktop_results, gu.wks_webVitals)

psi.update_psi_mobile(gu.urls_list, gu.wks_pageSpeed)
psi.update_psi_desktop(gu.urls_list, gu.wks_pageSpeed)

<<<<<<< HEAD
mft.update_mobileFriendlyTest()
=======
# mft.update_mobileFriendlyTest()
>>>>>>> cc12a95c7e1e4a336a9403adfdcb79397b0987ed
