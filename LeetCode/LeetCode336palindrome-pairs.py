#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 8:24 AM
# @Author  : Slade
# @File    : LeetCode336palindrome-pairs.py

'''
给定一组唯一的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。

示例 1:

输入: ["abcd","dcba","lls","s","sssll"]
输出: [[0,1],[1,0],[3,2],[2,4]]
解释: 可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
示例 2:

输入: ["bat","tab","cat"]
输出: [[0,1],[1,0]]
解释: 可拼接成的回文串为 ["battab","tabbat"]
'''

'''oot'''


class Solution1(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        ans = []
        for start in range(len(words)):
            for end in range(start + 1, len(words)):
                if (not words[start] and not words[end]):
                    continue
                condition1 = not words[start] and words[end] == words[end][::-1]
                condition2 = not words[end] and words[start] == words[start][::-1]
                merge_method1 = words[start] + words[end]
                merge_method2 = words[end] + words[start]
                condition3 = merge_method1 == merge_method1[::-1]
                condition4 = merge_method2 == merge_method2[::-1]
                if condition1 or condition2 or condition3:
                    ans.append([start, end])
                if condition4:
                    ans.append([end, start])
        return ans


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        lookup = {w: i for i, w in enumerate(words)}
        ans = []
        for i, w in enumerate(words):
            for idx in range(len(w) + 1):
                fri, las = w[:idx], w[idx:]
                '''bbc | c'''
                if fri[::-1] == fri and las[::-1] != w and las[::-1] in lookup:
                    ans.append([lookup[las[::-1]], i])
                '''acc | a'''
                if fri[::-1] != w and las[::-1] == las and fri[::-1] in lookup:
                    if idx ==len(w):
                        '''fir 和 last在idx=0和len(w)是一样的,只是交换了一下'''
                        continue
                    ans.append([i, lookup[fri[::-1]]])
        return ans


if __name__ == '__main__':
    print(Solution().palindromePairs(
        ["bchcfehaiaajbibjeh", "b", "abfcgcgechbci", "eiefcgaedcg", "iccci", "diaijheecaied", "idgc", "iighhebjia", "f",
         "fbhgggfgj", "daddiidfahi", "fbafdbfcjbgifbeg", "hag", "iaedbjfhff", "agigcfajfgbijc", "ea", "idacbjda",
         "ffgcbhgaghgcfj", "hcagid", "ajdadjefejbeh", "bdbgjd", "dhdcjghahc", "djacchdgebcgehjfgjfj", "ggaaicg", "gj",
         "cbdcgfbijdihjgj", "aghaicgchaiij", "idajacfbabhigaa", "jdgechbggeddjdc", "jjdjdihhdjfafff", "jghfhi", "aih",
         "bf", "digdgfhfdgjjgdc", "baf", "daiadgeagjbibih", "cidjbdgjafibbejbbic", "caaecgbecegdfiegbeii", "icchgffd",
         "jbcjajadgjcgaiabjgfd", "fcebbgahjieiicegaicc", "gdeg", "gehfchfebbdegaahifeg", "cfbaibeiicd",
         "idjdbahdagjiiaeff", "ghjca", "dfgabheifhffa", "ecfeefiicihg", "bjfjaefffdgaaefaaebh", "cjf", "gdbgce",
         "cdihdcdadechhejbhidg", "dfhgdgjfjeigfgca", "idcjhgicihebabbjj", "fbegafiha", "jaadeede",
         "ffefjjdfdccfgicgiih", "jfcaibgf", "g", "jjacejd", "ib", "ifiejbcfgjcefbajif", "ehbgcghhaicj", "bejd",
         "ifeagedcegefbhb", "ccjcbbjdeb", "fabaee", "aighgdffcch", "bjchjgfbh", "gfjgeeeehafgj", "egcafchgbg",
         "hfabbaabjghfeagadh", "cacejai", "fjieabfdhjjjccge", "diaeafjjcheb", "dd", "fbfhggbbjhgcdbeab", "gffhaahg",
         "feicdb", "gejbfhjfchhefcie", "ahdbcb", "jie", "eadagjbfhgf", "dajcdigeaia", "ifiba", "ihhhgj",
         "fafdbfbaefffhaccajh", "hicdecgbaacefch", "efdddjacacc", "dcaddfcejiahfdjieea", "ebcceejcbjfa", "cgij",
         "gihhjjbeidadcggbddc", "ififggggbgfghidd", "jefiecejjhjf", "gdc", "fjaifddeihdeeahae", "dhbdbfhgjjcc",
         "jidihhafbgcd", "bjhhgdbijhjgacebid", "cgjbedadajicjedfg", "jae", "hjjeaghfjg", "gjhggaigcdj",
         "eehbadeieigicg", "dgffcfg", "daefgh", "def", "ji", "jecgijhcdjhgbjgjdejd", "ebgbcigah", "jhije",
         "hjadadgffac", "dbajjfigfhigcaebheba", "hjgi", "fchbidbbfb", "hgbeigfdid", "ffbfebhbdhjidcb",
         "cgfdgdaffbgchgc", "acbg", "gaifbgjhbcjhcfij", "bafbh", "bagd", "cibbihhbdaghdhfajcf", "e", "cfgafaich",
         "cifgddbibbd", "jhadg", "jcbjefjc", "ehahcbhfdiecjeja", "gehgbfjbccg", "jbibjcfdh", "baiafgdfejjhd",
         "idicfjaiaiabbiacfjgh", "efccfgcg", "ia", "fgdad", "dijcfddaafehffbgf", "ahibgaaeebh", "diefidijhbhbiagg",
         "ejedbicfifcg", "fe", "ajacebfjgaddedhaaf", "fdbjiccbfaaej", "dhgg", "egdidaeai", "adhgiihdedicjfdehaia",
         "cciehcgb", "d", "agdgieidbhgeeghieed", "aa", "daiajfdediagii", "gidcacdfchdhfffjfbb", "ciiefdjddjdfjfaj",
         "ahjicijeidaghbabdci", "ecdjhaefa", "dbcfdicjaja", "cgchfjbecgaica", "hfehgag", "jiebba", "hdjfcbcjfejfdf",
         "a", "ejjacigaciabe", "fhadidbdbcgcbjdfff", "cefabgabgcbcdcghab", "iijjdcfccegfbffijhjj", "gicc",
         "acdgabefiacagfjj", "jeagjdgbhjcjichcfia", "efg", "baheidjhiigd", "fgfbfjfdcegahjigehi", "ciijbadgiab",
         "jiejfdjgfgeddighja", "ageadfhbhbdagdj", "icigbfcedaifa", "jedgd", "ibefh", "aihdf", "h", "jjceedjbedeefhcj",
         "jidecahidhbfagfdi", "jfbbdaddjicaefb", "fijadafecah", "hhiaecchcfjfbdchahb", "eaeifbbgbifhfajc",
         "bacdccccafdiac", "dhce", "ghgaciaijaaggf", "hgjfaagbebfefaed", "c", "cggdahhgcdbiiabeja", "ae",
         "dfdghfghefggie", "cijbbibahhjgjgggejcd", "cabddde", "egfiha", "bjjgdffedifadgdeh", "ifiiiaj", "dbbecjbcb",
         "bgheihchffg", "ecffhfaaggegiaj", "bjajhfjjajd", "dhhgiach", "dhieagagfhgbcjhdd", "cjabdc", "iiihihhdaghcd",
         "bceeffjagchfacdecge", "igicgggajjeeeii", "ieiighhjjjbdgb", "iacaaggibagcig", "bhgggcfhd", "gbiecffeccfchegea",
         "gcbjf", "fjdffjedcaifdffhaa", "djajf", "fgbgja", "aaid", "aiidahjaj", "ddfiehbbbba", "hafche", "icaagch",
         "cifjec", "dhchghf", "bhdegahijbgjafgb", "bihjciibgj", "eiej", "aeijdga", "eejcgjhjajfaeaj", "jjbiageg",
         "ejabjfhghfcja", "hdjjhe", "eabbbbcbcfedecaeb", "jh", "jjbdhicigaciagg", "gigjfgbj", "diaffbf",
         "fhfaaijbjdceeaajd", "ghagji", "ighefbhjiijedff", "fhd", "eagcgdgig", "edjbdjdbfe", "eeffbjjchj",
         "dagccfgcjgjigcaid", "ibdafbedhdj", "cefjejjedjdbcaejabd", "bb", "hiiiiebeaejbfiica", "bbcea", "ab",
         "aaccbhbjghgeef", "iddbdddghfbdcdhifj", "igjbabddgeddcjjafaa", "adecbadddj", "dcbfffjjdaigibig",
         "iichgcajdbiiie", "ebdjdjiejeegi", "hbabhdiihgchhbjj", "jdggdejegebbahdf", "ai", "hcgjeeggadeccca",
         "bfdjaceiegbcjfjc", "ihcacegbdcc", "bafi", "ihbgcjaaggefbjdjd", "ciihadhbagihbafcb", "habfhagdfbjh",
         "hgdggccecfgjgigb", "eigebefahdfdihf", "bhg", "fajfabdedabe", "abedcjhb", "iicjadf", "aihcfbdefhhaiegaccie",
         "ehajc", "gfediahah", "behjcaafccggecgiic", "babffia", "afdhdcbiffa", "icfcfj", "hcbffghiaaa", "acefbfggg",
         "hg", "fbihacadeadibh", "ihjfgcgjjigcd", "beffiihhceddgbhgjcg", "hhdcdfhaehidbghajbdh", "debgeejbh", "ahcbh",
         "cagefihe", "jfggbhbhcebibiahea", "febagdhgiefbfbec", "ddcifhhbjachafgeeg", "jaadijbiebfdbeibeje",
         "fgjhdabghjce", "fhicfg", "jfdcbhachhg", "acfejfggi", "cj", "hfjbbb", "hgggjggff", "jefeffcffddiic",
         "cedaefighhfggjghjgdb", "bihhhc", "ieacgjjbgjifca", "aaibfbhgeicca", "acifbfgaihii", "baddafg", "fhajfec",
         "ihffbhddajcce", "jhefcdiiheghgcj", "degjcgah", "dde", "jaabfdjhadaif", "gba", "hfebaaib", "fgecefcghdh",
         "jjgi", "hdfchjgdjbcjfehc", "fhfeaeig", "fgdcibbjafdaf", "agchicajgjdgaibadfb", "gfehbf", "ichcbebhgjcghhihi",
         "bigciceiad", "ebdiejehiabbgcc", "jedjjfdhcicf", "geijjbjjdiifcc", "hhceddceghjgfebfbf", "gffjbbcgfaefcgcge",
         "jigbb", "je", "aaicdjcfjbh", "jdidcgde", "dhbdjcbfgjaagabb", "bacfjcbiec", "fceihggahacffbhf", "jgjdjg",
         "hgccfdbbjdjbfjecfdia", "bfhhbjfijdhaicih", "bjjdjjjhebhfgjeagef", "caji", "daaidgjedfcj", "efdhf",
         "eaihabgcahafaabg", "jfhebfjghaabhfjhcahh", "ag", "ajfbacfbdbedii", "fjgijffhcjffj", "dea", "ddahaiage",
         "iicdjabigggjhe", "ieghaihjibj", "bdj", "cbidbcehdg", "aibiihfeg", "ee", "jgi", "bdcjabeccjgheb", "hhbj",
         "fafdfhajjjeabcfcgdie", "hhehja", "agdcfdfjh", "fafa", "afghddadcfbjbcifgh", "jibj", "bbacfg", "bbadffaee",
         "dicjhbidi", "gh", "jbajigbfeagheegjdaa", "aicbedbah", "dcfdjiaeccgbajfjgea", "iaahhcchbgfgejjhfehc",
         "cecdgjfjedfjhcc", "faehaibidhcebcfcb", "hd", "hddeegbccdadbjfjb", "bdjadjifj", "aacaehbacieij", "acigdbgbh",
         "cjjjjhjcfi", "gfbihbdfe", "gijcficfi", "fhefedgchhhfdcgcjie", "igbbcddfjadahajdjc", "bceagahcfdghjj", "jdcja",
         "abbd", "hhadcbihcae", "abdhib", "dbaidecejchbih", "fbaccdajcbfij", "fdcdjaddafbgj", "dcci", "i", "aheecai",
         "egcghfjb", "ggedfbg", "ecjeafhffcfjjfcc", "gijggfediachjegbjdfe", "bjdbccagchgcbcec", "iejddfcfdihg",
         "abcfhdfadijaecihgih", "abebjchchjjbbe", "bdehgfif", "cjeijfacee", "hbaadeicacccb", "gfdbjgaghj", "igehbcchj",
         "jjia", "caebafdgbcgcfg", "ibdafihhej", "eedeicegjeddaacgecd", "aagbfhhfbhhbejjbjajf", "bchdgcgjihaaidg",
         "ciccadeg", "gjhidcjdcffhfcef", "bdcahhggeb", "jffciecfjbjcebf", "gbabjiajgcjhfehd", "jdajfbicjggigbj",
         "ebfga", "jeejacgj", "ibceidcedgghf", "hiabbbijejhcigjjfi", "dgaehccicahfcgic", "bfaejg", "daejhfgiegafciihaj",
         "jgfcfeeeaeigfadhh", "fjejdficgcbhhifbg", "jhaiagdiffbadccf", "ehbaihbhfccfd", "hhehjdffbijcgedb", "biiij",
         "fbbbhebjfjjgddfffege", "jdijj", "ibfgebajj", "cgadacabfhhhdacfj", "hahgcjafiagajifje", "if", "abg",
         "bjfjfhbbc", "dcijidcajicbedeade", "dejbdchchgdecji", "hfafjfi", "edjbbadfaghffc", "eibdbebgdegcggggih",
         "hcbgaechgdcgdbiegiaf", "eeficfhhagbebjchbhff", "edjcbjjbd", "hihehfbaaabjgbc", "beac", "jcadhajfedgabhjfchaa",
         "bhff", "djjhcfcjiecjhbef", "iddgjfh", "fcejjfcajicj", "fheigahegeaghifgf", "agdcejc", "dad",
         "cdecjhabajcchebci", "jjcjji", "gbghghfcfdjefiiaici", "hhdhdfcgcae", "ecibiajjceeecgacc", "heehfijaaf",
         "cecjhbfhgc", "gahheficaedicfhiicg", "beefejaeabhaddbid", "ah", "chdcjdhg", "eecjdhjhfibaifcc", "aiei",
         "dbegchjcecba", "bbchffaj", "j", "habidjegh", "icffghbeghdgecfi", "ei", "bfbj", "egfccfdiihhibhgieff",
         "fbajjgagihgbhegjbj", "haijdgbcfgaaabefccd", "ahib", "ebfhebcidhae", "gfchjebhbifcagdheha",
         "eggdddaijjhfeeibfid", "jij", "edb", "eeac", "iehifcefib", "bhcfihhecjffg", "ejfjjfif", "iccjjfgjggb",
         "fcjebbijafj", "hgbdjcdgciea", "cgafdghfacf", "dijbjidibdda", "bcehicegfajbfj", "ifcicchegbihe", "ffhhg",
         "aeehjfchhehaceaheded", "ahgi", "dcbafhcacfachdg", "ihgaigaaae", "hgicchcegjibb", "egcechhiah",
         "ggibfefibjbiha", "gf", "hefje", "ehcffcecfeifdgfbf", "bebeadfecdchheiegj", "jfaiggjgb", "ehhjif", "ddca",
         "edjcgbdhhjheiahi", "gghhbheeee", "fdjec", "ja", "cbgbfbdfdg", "dhhhbchchcdif", "ciajfggefjhifbcb", "iedgj",
         "hihchciicgibdbbihbec", "jccgiijbcc", "idifj", "iijf", "hfhibfadhcjf", "ihgjhgieiijgecaaag", "cdbachf",
         "bbfhaibabgiadfgdhi", "fgciifcheihh", "adajhhaa", "gaiegfdafgbcif", "ebbicfifdhgjf", "idbeigaibcdjih",
         "hiddfcbcb", "cjibcebebdacfa", "fihjiecihfjbbhdfig", "djedejgcgagbcgjib", "bab", "bdcecjdejdhegffi", "gedd",
         "fjddjbhhjj", "ifgfcjcfcai", "ahh", "ifbhfhdejjejadadh", "cd", "ddhibh", "hcgibciicfa", "jefdjja",
         "geegghfbbfcaeifff", "giijcdh", "dei", "jjjiiejfdjfhcb", "ebeefidgjhedeeddjg", "behhhgfchicdddhfebic",
         "hgdeiahjebee", "ibbhieaiihaib", "jiagegca", "edejecjhc", "iehc", "bgjbdfafadeihgegb", "jjbejad", "iga",
         "ggfcfjf", "badad", "hbaiidffje", "fhdebfggeeadejadjaif", "gbfjfegefaijbd", "bihigjghi", "bifeabifgfbif",
         "ifh", "hjeceefhje", "ddbcihgj", "edcifi", "cfaacaddhaf", "egj", "debccccaf", "ciiefhdjfdiei",
         "ccfjdhbghicdac", "hfbbhcjciei", "geghaegdhj", "igcbdehegebj", "jddhjeaj", "ibffhiaa", "hbdijhbfcbfg",
         "ecjbeijgbdfaj", "fcddchgibadaghgdfe", "cedach", "gjeea", "idffiafigdbhaa", "edccj", "ihgiahca", "gicieaeche",
         "jjgiiigbchbiie", "ccicf", "ibbbc", "ead", "egeedc", "ajjjhajjbhb", "chjj", "acdbjfhdcdbfggjdab",
         "ehjdbhicgajfgafagbc", "da", "faaegbi", "gdbbeajjiejdhijef", "ggdbbhjjaibf", "ffej", "effgebjeejadecij", "df",
         "jefgcdie", "hicecceichiibb", "cej", "jfafgihdiafce", "jjdbihcibii", "agiigbgfdbejdd", "iedaajbdcciigfdc",
         "fecjccidgafbjbddff", "dhfejdeccihb", "cgffagcafceib", "ihifihf", "jdibafaejdjb", "jeigdgeei",
         "iehdehhccfchbbhgcejj", "effbhfihac", "iiafgada", "ebdgeggigcfgbiabg", "ehbidfji", "jcbjid", "cihfecddbabgjj",
         "jdgidjeiegfjhh", "ghfgbcghbidhjgegfa", "jdbefebhjefgbbdih", "aacahh", "fjci", "cebcddiihbeg",
         "bfajdgahdifbdbfchidc", "iafjjejehhdghidjfbb", "feaaicecedefcdjff", "ihf", "ibhebfighfjbbbcge",
         "cjhaddgdhidbgefdege", "bbcgdgabddjhc", "jbeabgcffcei", "eg", "didaafcdehgbba", "biifijf", "ajecbaefgdhff",
         "efagdcecdijefej", "ejecjfcdafa", "ifjjigbicacbajbh", "bhbiigbicedjai", "ghcjjgfc", "gfdcaceaeabjbgi",
         "djibiccadahaeichfe", "jjjeebdgbaaigfebe", "aibadijjefjhechd", "afjiddaidibhbjaf", "gaiijeffjjbbhjehe", "cec",
         "fagd", "bidga", "eiahehbdebcibfcj", "ajgbcecfgfbacbdd", "cdih", "cdei", "abe", "dfechhhgiiibj", "biijaeehjei",
         "ecaiadjgadbcbijidfi", "aibjgaachiadge", "eccgbbadddfidifgbaa", "dicbbjiedeiafehebgih", "edeaeihjib", "gddiac",
         "aeadjiecia", "abjehchdbbddjgichjib", "gbbbg", "hbbcfcfdhjide", "jdfiiefjjjhgaifebd", "jabbffeag",
         "bagihjaecifgbdfgjf", "hiac", "fcjafjdiagfce", "difjbedficc", "ggijgegagcijjdh", "ihihg", "echjbjdaejjbdi",
         "afhijjd", "idigc", "gehfgbg", "agghaggbfdega", "dhiddchjbdgccdiicb", "ifcc", "jfjd", "fdagciafieidibjbd",
         "jifbjdhcdgbchhc", "bba", "cfiffifbiaiic", "ced", "cbeeahdhfefebeicbbh", "ebaifidc", "ghach",
         "ccedjfeefieaahcihc", "hfhbgiicijffj", "ijchegejhgcgcfc", "gfbagghgejdijgge", "hfghjffee", "acicfjifjj",
         "ehfca", "fhabgddc", "heifhfgahfefjbccafaj", "ebfaibii", "aghggjgbdejigbgjfga", "gjaj", "gficdc",
         "ififeajgicgdgi", "iaiaigihhi", "ejdbdacaccbaaghidi", "ijigefdjaaeaijhbga", "dgdgcfciaghi", "ddgcaba", "fa",
         "bhfgifghc", "bfc", "jfdjaabc", "ecihfdaajjcd"]))
