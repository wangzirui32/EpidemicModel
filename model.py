import time
import random
import json

def load_config():
    with open("config.json", "r", encoding="UTF-8") as f:
        config = json.load(f)
    return config

class EpidemicModel():
    def __init__(self) -> None:
        # 读取配置文件
        config = load_config()
        # 自定义参数
        # ===================================== #
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
        
        # 初始化参数
        # ===================================== #
        # 天数 Day
        self.day = 1
        # 感染者总数 Cases
        self.cases = self.IPQ+self.IPNQ
        # 感染人数占人口总数的比例 Proportion of infected persons to total population
        self.PIPTP = self.cases / self.total_people

    def update(self):
        self.update_measures()
        self.update_cases()
        self.update_data()

    def update_cases(self):
        for i in range(self.IPNQ):
            for j in range(self.ADCP):
                if random.random() < self.IR:
                    self.IPNQ += 1

    def update_measures(self):
        for i in range(self.IPNQ):
            if random.random() < self.QR:
                self.IPQ += 1
                self.IPNQ -= 1

    def update_data(self):
        self.day += 1
        self.cases = self.IPNQ + self.IPQ
        if self.cases > self.total_people:
            self.cases = self.total_people 
        self.PIPTP = self.cases / self.total_people


    def output_msg(self):
        print("="*40)
        print(f"Day {self.day}")
        print(f"总人数：{self.total_people}人")
        print(f"感染者人数：{self.cases}人")
        print(f"每人日均接触人数：{self.ADCP}人")
        print(f"病毒携带者占比：{self.PIPTP*100:.2f}%")
        print(f"病毒感染几率：{self.IR*100:.2f}%")
        print(f"隔离感染者数量：{self.IPQ}")
        print("="*40)
    
    def run(self):
        try:
            while True:
                self.output_msg()
                if (self.IPNQ+self.IPQ) > self.total_people:
                    print("所有人均被感染！")
                    break
                if (self.IPNQ == 0):
                    print("疫情得到控制！")
                    break
                self.update()
                time.sleep(3)
        except KeyboardInterrupt: pass
        print("模拟结束........")

if __name__ == '__main__':
    model = EpidemicModel()
    model.run()