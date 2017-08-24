#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of fionautil.
# http://github.com/fitnr/fionautil

# Licensed under the GPLv3 license:
# http://http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, Neil Freeman <contact@fakeisthenewreal.org>

from unittest import TestCase as PythonTestCase
import unittest.main
import os.path
from fionautil import feature

shp = os.path.join(os.path.dirname(__file__), 'fixtures/testing.shp')
geojson = os.path.join(os.path.dirname(__file__), 'fixtures/testing.geojson')


class TestFeature(PythonTestCase):

    def setUp(self):
        self.polygon = {'properties': {'a': 1, 'b': 2}, 'geometry': {'type': 'Polygon', 'coordinates': [[(-122.002301, 37.529835999999996), (-122.002236, 37.529908), (-122.001506, 37.529309999999995), (-122.002196, 37.529679), (-122.00236, 37.529773999999996), (-122.002301, 37.529835999999996)], [(-156.71787267699898, 21.137419760764438), (-156.76604819764898, 21.06517681773707), (-156.8864840998058, 21.04913411712499), (-157.07113192831787, 21.105330956858555), (-156.71787267699898, 21.137419760764438)]]}}

        self.linestring = {'geometry': {'type': 'LineString', 'coordinates': [(1698558.6560016416, 785359.5722958631), (1698570.6255255828, 785357.1199829046), (1698592.7188758815, 785353.618717982), (1698615.888545638, 785342.774320389), (1698632.1053597904, 785336.6905814429), (1698651.8725316962, 785330.0421180109), (1698659.045153662, 785327.3537529241), (1698688.1001785155, 785316.4641486479), (1698696.6319864516, 785313.4574198754), (1698717.936275069, 785303.1641204398), (1698733.601512783, 785295.2805483269), (1698757.090320928, 785281.0787615285), (1698773.2214488257, 785270.9157159382), (1698802.13278612, 785251.4878775944), (1698839.0495838472, 785227.758052662), (1701103.0715925542, 785570.0575142633), (1701117.0415831083, 785569.3192712615), (1701143.1992729052, 785566.1717272209), (1701168.650131336, 785560.3315072984), (1701209.706061085, 785548.4685232819), (1701250.512021864, 785532.6336759274), (1701281.5801281473, 785515.853762881), (1701310.5929042343, 785499.6991391898), (1701378.6116007813, 785459.892916804), (1701445.1270219584, 785422.3276661132), (1701482.1400952877, 785402.5158508102), (1701506.6506188242, 785391.8440056049), (1701523.390860305, 785385.4644141722), (1701559.0541053142, 785373.9359225394), (1701572.477673862, 785369.6783910012)]}}

        self.multipolygon = {'geometry': {'type': 'MultiPolygon', 'coordinates': [[[(-156.71787267699898, 21.137419760764438), (-156.76604819764898, 21.06517681773707), (-156.8864840998058, 21.04913411712499), (-157.07113192831787, 21.105330956858555), (-157.28789752278652, 21.081250571840183), (-157.30394879695828, 21.137448432663767), (-157.2477475061229, 21.161530451508398), (-157.23169415834994, 21.233776323139818), (-157.16747148788883, 21.19364045634365), (-157.00690374246722, 21.18561063798249), (-156.95873348755612, 21.209693513430512), (-156.94268251253186, 21.161526867134565), (-156.71787267699898, 21.137419760764438)]], [[(-156.1960454124824, 20.631649407365213), (-156.27631740739284, 20.583483860915248), (-156.3967349429455, 20.567426981472988), (-156.43687923087785, 20.623621217336662), (-156.46097189319752, 20.727981087256364), (-156.49307474018514, 20.792204281510333), (-156.5251935717042, 20.776149657497466), (-156.63758660416465, 20.80826091204387), (-156.69378263402297, 20.912624010061208), (-156.65363600731771, 21.016985049562912), (-156.5974396197875, 21.041064705415824), (-156.5251916458635, 20.98487016377238), (-156.47702205254387, 20.89656513911172), (-156.3566035032919, 20.9447263610079), (-156.26026336307226, 20.928671268747912), (-156.01139245254785, 20.800225321607478), (-155.98731705257018, 20.752061631687628), (-156.0435115425545, 20.65573259996677), (-156.1318089039728, 20.62362291867985), (-156.1960454124824, 20.631649407365213)]], [[(-157.03905067093797, 20.928706972385005), (-156.91058584516276, 20.928718617694337), (-156.80620534154883, 20.84041861217258), (-156.81422569781648, 20.7922527172797), (-156.88648717839553, 20.73604940916775), (-156.96676559866026, 20.728020731638775), (-156.9908634657756, 20.792237151462064), (-156.9828263229743, 20.832377626807837), (-157.05509821197901, 20.880538425907034), (-157.03905067093797, 20.928706972385005)]]]}}


    def testCompound(self):
        assert feature.compound(self.linestring) == False
        assert feature.compound(self.multipolygon) == True
        assert feature.compound(self.polygon) == True

    def testFieldContains(self):
        test1 = feature.field_contains_test({'a': (1, 2, 3)})
        test2 = feature.field_contains_test({'b': (7, 8, 9)})

        assert test1(self.polygon) == True
        assert test2(self.polygon) == False

if __name__ == '__main__':
    unittest.main()