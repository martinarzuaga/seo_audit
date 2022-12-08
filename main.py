import credentials.loging_to_gs as lgs
import modules.update_velocidad as ud
import modules.get_urls as gu
import modules.update_cache as uc
import modules.request_tests as rt
import modules.update_code_ratio as ucr

lgs.log_to_gs()

mobile_results = rt.request_tests_mobile(gu.urls_list)

desktop_results = rt.request_tests_desktop(gu.urls_list)

ud.update_velocidad_mobile(mobile_results, gu.wks_velocidad)

ud.update_velocidad_desktop(desktop_results, gu.wks_velocidad)

uc.update_cache(mobile_results, gu.wks_cache)

ucr.update_code_ratio(mobile_results, gu.wks_velocidad)
