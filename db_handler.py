from pymongo import MongoClient


class SignMongoDB(object):

    def __init__(self, username: str):
        self.client = MongoClient("mongodb://localhost:27017/")
        database = self.client["signweb"]
        self.collection = database["users"]
        self.username = username
        if not self.collection.find_one({"username": username}):
            self.collection.insert_one({"username": username})

    def to_get_cookie(self) -> dict:
        """从数据库内取出cookie"""
        return self.collection.find_one({"username": self.username}, {"cookie": 1.0})['cookie']

    def to_save_cookie(self, cookie: dict):
        """保存cookie到数据库"""
        # 如果cookie失效，先从数据库删除旧的cookie
        # 再保存新的cookie
        # todo
        self.collection.update_one({"username": self.username}, {"$unset": {"cookie": ""}})
        self.collection.update_one({"username": self.username}, {"$set": {"cookie": cookie}})

    def to_get_all_classid_and_courseid(self) -> list:
        """获取此用户所有的课程id"""
        cursor = self.collection.find_one({"username": self.username}, {"cclist": 1.0})
        try:
            return cursor['cclist']
        except:
            return []

    def to_save_all_classid_and_courseid(self, cclists: list):
        """保存此用户所有的课程id"""
        for cclist in cclists:
            self.collection.update_one({"username": self.username},
                                    {"$addToSet": {"cclist": cclist}})

    def to_save_istext_activeid(self, activeid: str):
        # 保存已签过到的任务id
       self.collection.update_one({"username": self.username}, {"$addToSet": {"activeid": activeid}})

    def to_get_istext_activeid(self) -> list:
        """获取前10个已签到activeid"""
        sort = [(u"_id", -1)]
        res = self.collection.find_one({"username": self.username}, {"activeid": 1.0}, sort=sort, limit=10)
        try:
            return res["activeid"]
        except:
            return []

    def set_test_data(self):
        self.collection.insert_one({"username": self.username, "cookie": 11111, "activeid": [1,2], "classid": [8,9], "courseid": [8,9]})


if __name__ == '__main__':
    s = SignMongoDB("222")
    # s.to_save_istext_activeid("123")