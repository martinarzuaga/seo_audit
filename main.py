import credentials.loging_to_gs as lgs
import modules.get_audit_urls as gau
import modules.request_tests as rt
import modules.update_velocidad as ud
import modules.update_cache as uc
import modules.update_code_ratio as ucr
import modules.update_web_vitals as uwv
import modules.update_pagespeedinsights as psi
import modules.update_mobile_friendly_test as mft
import modules.meta_tags as mt

gc = lgs.log_to_gs()

# Web Scraping Modules
mt.run_meta_tags_test(gau.urls_list, mt.get_audit_sheet(gc))

mobile_results = rt.request_tests_mobile(gau.urls_list)
desktop_results = rt.request_tests_desktop(gau.urls_list)

# ALL TESTS
ud.update_velocidad_mobile(mobile_results, gau.wks_velocidad)
ud.update_velocidad_desktop(desktop_results, gau.wks_velocidad)
ucr.update_code_ratio(mobile_results, gau.wks_velocidad)

uc.update_cache(mobile_results, gau.wks_cache)

uwv.update_web_vitals_mobile(mobile_results, gau.wks_webVitals)
uwv.update_web_vitals_desktop(desktop_results, gau.wks_webVitals)

psi.update_psi_mobile(gau.urls_list, gau.wks_pageSpeed)
psi.update_psi_desktop(gau.urls_list, gau.wks_pageSpeed)

mft.update_mobileFriendlyTest()
