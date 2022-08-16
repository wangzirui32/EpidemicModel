<h1 style="text-align: center">传染病传播模拟</h1>
<p style="text-align: center">
<img src="https://img.shields.io/static/v1?label=Program&message=Python&color=blue"/>
<img src="https://img.shields.io/static/v1?label=Python&message=3.9.5&color=yellow"/>
<img src="https://img.shields.io/static/v1?label=Version&message=1.0.0&color=red"/>
</p>

该项目使用Python开发，依赖Python的内置库，主要用于模拟传染病的传播，下面是可以自定义的模拟参数：
```py
# 总人数 Total People
self.total_people = config.get("total_people")
# 未隔离的感染者 Number of infected persons not quarantined
self.IPNQ = config.get("IPNQ")
# 已隔离的感染者 Number of infected persons quarantined
self.IPQ = config.get("IPQ")
# 平均每人每日接触人数 Average daily contact number per person
self.ADCP = config.get("ADCP")
# 感染几率 Infection rate
self.IR = config.get("IR")
# 检疫效率 Quarantine rate
self.QR = config.get("QR")
# 治愈率 Cure rate (暂未开发)
#self.CR = config.get("CR") 
```
这些参数可以在`config.json`中更改。
目前仅支持在终端中查看结果，后续会改进。