class Gun:
    def __init__(self,model,count):
        Gun.model = model
        Gun.count = count
    def add_bullet(self,count_add):
        Gun.count = Gun.count + count_add
    def shoot(self):
        if Gun.count > 0:
            print('子弹发射')
            Gun.count -= 1
        else:
            print("没子弹了")

class Soldier:
    def __init__(self,name,gun):
        Soldier.name = name
        Soldier.gun = gun
    def __name__(self):
        return "士兵%s持有枪支%s" %(Soldier.name,Soldier.gun)
    def fire(self):
        if Gun.count > 0:
            print('开火')
            Gun.shoot(gun)
            print("子弹剩余%d" %Gun.count)
        else:
            print('没子弹了')

gun = Gun("AK47",3)
print(gun)
Xu = Soldier("许三多","AK47")
print(Xu)
Gun.add_bullet(gun,3)
Soldier.fire(Xu)

# 类属性和类方法就是针对类对象定义的属性和方法，在类方法中可以直接访问类属性和其他的类方法；
# 除类方法外类中定义的其他方法为实例方法

class Tool(object):  # 定义类，object为父类
    count = 0  # 定义类变量count
    @classmethod  # 修饰器，表明类方法
    def show_tool_count(cls):  # 类方法参数必含cls
        print("内含工具的数量%d" %Tool.count)
    def __init__(self):
        Tool.count += 1

# 开发时，如果需要在类中封装一个方法，这个方法：
# 需要访问实例属性，定义为实例方法（以self作为第一个参数）
# 需要访问类属性，定义为类方法
# 实例方法与类方法均不需要访问，则定义为静态方法即可（无需参数）

class Dog(object):
    @staticmethod
    def run():
        print("小狗跑步")

Dog.run() # 使用类名.方法名调用静态方法，无需创建实例

class Game(object):
    highest_score = 0
    @classmethod
    def show_score(cls):
        print("历史最高分为%d" %cls.highest_score)
    def __init__(self,name):
        self.name = name
    def start_game(self):
        print("%s开始游戏" %self.name)
    @staticmethod
    def help():
        print("游戏说明")


Game.help()
Game.show_score()
player = Game("玩家1")
player.start_game()