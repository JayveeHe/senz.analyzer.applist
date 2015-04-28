# -*- encoding:utf-8 -*-
__author__ = 'zhongziyuan'

import json
from math import sqrt
from sys import maxint


class InfoGetter:

    def __init__(self, dict_file):
        self.judge_dict = InfoGetter.load_dict(dict_file)

    @staticmethod
    def load_dict(dict_file):
        f = open(dict_file, 'r')
        content = f.read()
        f.close()
        res = json.loads(content, encoding="utf-8")
        return res

    def get_labels(self, info):
        if not isinstance(info, list):
            print 'Input data must be list !'
            return {}
        res = {}
        for label, classes in self.judge_dict.items():
            label_class = self.get_class(classes, info)
            res[label] = label_class

        return res

    def get_class(self, classes, info):
        info_vec = {}
        degrees = classes.values()[0].keys()
        for app in degrees:
            if app in info:
                info_vec[app] = 1
            else:
                info_vec[app] = 0

        max_sim = -maxint
        max_class = ''
        for oneClass, value in classes.items():
            v1 = 0
            v2 = 0
            v1_v2 = 0
            for k, v in value.items():
                v1 += v ** 2
                v2 += (info_vec[k])**2
                v1_v2 += v * info_vec[k]
            sim = v1_v2/sqrt(v1*v2+0.001)
            if sim > max_sim:
                max_sim = sim
                max_class = oneClass

        return max_class


if __name__ == '__main__':
    i = InfoGetter("dict.json")
    print i.get_labels(["com.kplus.car", "cn.buding.martin"])
