import itertools
import json
from parse import load_dataframes
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import io
from sklearn.feature_extraction.text import CountVectorizer
import seaborn as sns
import shutil
import os

data = load_dataframes()
term_w = shutil.get_terminal_size()[0] - 1
separater = "-" * term_w

df = data["stores"]
# # df = df[df["address"] != ' ']
# ai = df["address"].values
# ai = list(ai)
# print(ai)



def area_category(area):
###### 서울#################################################################3
    A = ["서울특별시 종로구", "서울시 종로구", "서울 종로구"]
    for a in A:
        if a in area:
            return "서울중구"

    B = ["서울특별시 중구", "서울시 중구", "서울 중구"]
    for b in B:
        if b in area:
            return "서울중구"

    C = ["서울특별시 용산구", "서울시 용산구", "서울 용산구"]
    for c in C:
        if c in area:
            return "서울용산구"

    D = ["서울특별시 성동구", "서울시 성동구", "서울 성동구"]
    for d in D:
        if d in area:
            return "서울성동구"
    
    E = ["서울특별시 광진구", "서울시 광진구", "서울 광진구"]
    for e in E:
        if e in area:
            return "서울광진구"

    F = ["서울특별시 동대문구", "서울시 동대문구", "서울 동대문구"]
    for f in F:
        if f in area:
            return "서울동대문구"
    
    G = ["서울특별시 중랑구", "서울시 중랑구", "서울 중랑구"]
    for g in G:
        if g in area:
            return "서울중랑구"
 
    H = ["서울특별시 성북구", "서울시 성북구", "서울 성북구"]
    for h in H:
        if h in area:
            return "서울성북구"

    I = ["서울특별시 강북구", "서울시 강북구", "서울 강북구"]
    for i in I:
        if i in area:
            return "서울강북구"

    J = ["서울특별시 도봉구", "서울시 도봉구", "서울 도봉구"]
    for j in J:
        if j in area:
            return "서울도봉구"

    K = ["서울특별시 노원구", "서울시 노원구", "서울 노원구"]
    for k in K:
        if k in area:
            return "서울노원구"

    L = ["서울특별시 은평구", "서울시 은평구", "서울 은평구"]
    for l in L:
        if l in area:
            return "서울은평구"

    M = ["서울특별시 서대문구", "서울시 서대문구", "서울 서대문구"]
    for m in M:
        if m in area:
            return "서울서대문구"

    N = ["서울특별시 마포구", "서울시 마포구", "서울 마포구"]
    for n in N:
        if n in area:
            return "서울마포구"


    O = ["서울특별시 양천구", "서울시 양천구", "서울 양천구"]
    for o in O:
        if o in area:
            return "서울양천구"

    P = ["서울특별시 강서구", "서울시 강서구", "서울 강서구"]
    for p in P:
        if p in area:
            return "서울강서구"

    QQ = ["서울특별시 구로구", "서울시 구로구", "서울 구로구"]
    for q in QQ:
        if q in area:
            return "서울구로구"

    R = ["서울특별시 금천구", "서울시 금천구", "서울 금천구"]
    for r in R:
        if r in area:
            return "서울금천구"

    S = ["서울특별시 영등포구", "서울시 영등포구", "서울 영등포구"]
    for s in S:
        if s in area:
            return "서울영등포구"

    T = ["서울특별시 동작구", "서울시 동작구", "서울 동작구"]
    for t in T:
        if t in area:
            return "서울동작구"

    U = ["서울특별시 관악구", "서울시 관악구", "서울 관악구"]
    for u in U:
        if u in area:
            return "서울관악구"

    V = ["서울특별시 서초구", "서울시 서초구", "서울 서초구"]
    for v in V:
        if v in area:
            return "서울서초구"

    X = ["서울특별시 강남구", "서울시 강남구", "서울 강남구"]
    for x in X:
        if x in area:
            return "서울강남구"

    Y = ["서울특별시 송파구", "서울시 송파구", "서울 송파구"]
    for y in Y:
        if y in area:
            return "서울송파구"

    Z = ["서울특별시 강동구", "서울시 강동구", "서울 강동구"]
    for z in Z:
        if z in area:
            return "서울강동구"


######대전#################################################################
    AA = ["대전광역시 동구", "대전시 동구", "대전 동구"]
    for aa in AA:
        if aa in area:
            return "대전동구"

    BB = ["대전광역시 중구", "대전시 중구", "대전 중구"]
    for bb in BB:
        if bb in area:
            return "대전중구"

    CC = ["대전광역시 서구", "대전시 서구", "대전 서구"]
    for cc in CC:
        if cc in area:
            return "대전서구"

    DD = ["대전광역시 유성구", "대전시 유성구", "대전 유성구"]
    for dd in DD:
        if dd in area:
            return "대전유성구"
    
    EE = ["대전광역시 대덕구", "대전시 대덕구", "대전 대덕구"]
    for ee in EE:
        if ee in area:
            return "대전대덕구"

######대구#################################################################
    AAA = ["대구광역시 동구", "대구시 동구", "대구 동구", "대구광역시  동구"]
    for aaa in AAA:
        if aaa in area:
            return "대구동구"

    BBB = ["대구광역시 중구", "대구시 중구", "대구 중구"]
    for bbb in BBB:
        if bbb in area:
            return "대구중구"

    CCC = ["대구광역시 서구", "대구시 서구", "대구 서구"]
    for ccc in CCC:
        if ccc in area:
            return "대구서구"

    DDD = ["대구광역시 수성구", "대구시 수성구", "대구 수성구"]
    for ddd in DDD:
        if ddd in area:
            return "대구수성구"
    
    EEE = ["대구광역시 달서구", "대구시 달서구", "대구 달서구"]
    for eee in EEE:
        if eee in area:
            return "대구달서구"

    FFF = ["대구광역시 달성군", "대구시 달성군", "대구 달성군"]
    for fff in FFF:
        if fff in area:
            return "대구달성군"
    
    GGGi = ["대구광역시 남구", "대구시 남구", "대구 남구"]
    for gggi in GGGi:
        if gggi in area:
            return "대구남구"
 
    HHH = ["대구광역시 북구", "대구시 북구", "대구 북구"]
    for hhh in HHH:
        if hhh in area:
            return "대구북구"

######광주#################################################################
    AAAA = ["광주광역시 동구", "광주시 동구", "광주 동구"]
    for aaaa in AAAA:
        if aaaa in area:
            return "광주동구"

    BBBB = ["광주광역시 중구", "광주시 중구", "광주 중구"]
    for bbbb in BBBB:
        if bbbb in area:
            return "광주중구"

    CCCC = ["광주광역시 서구", "광주시 서구", "광주 서구"]
    for cccc in CCCC:
        if cccc in area:
            return "광주서구"

    DDDD = ["광주광역시 북구", "광주시 북구", "광주 북구"]
    for dddd in DDDD:
        if dddd in area:
            return "광주북구"
    
    EEEE = ["광주광역시 광산구", "광주시 광산구", "광주 광산구"]
    for eeee in EEEE:
        if eeee in area:
            return "광주광산구"
        
        
    FFFF = ["광주광역시 남구", "광주시 남구", "광주 남구"]
    for ffff in FFFF:
        if ffff in area:
            return "광주남구"

######제주#################################################################
    AAAAA = ["서귀포시"]
    for aaaaa in AAAAA:
        if aaaaa in area:
            return "제주서귀포시"

    BBBBB = ["제주시"]
    for bbbbb in BBBBB:
        if bbbbb in area:
            return "제주제주시"

######인천#################################################################
    AAAAAA = ["인천광역시 동구", "인천시 동구", "인천 동구"]
    for aaaaaa in AAAAAA:
        if aaaaaa in area:
            return "인천동구"

    BBBBBB = ["인천광역시 중구", "인천시 중구", "인천 중구"]
    for bbbbbb in BBBBBB:
        if bbbbbb in area:
            return "인천중구"

    CCCCCC = ["인천광역시 서구", "인천시 서구", "인천 서구"]
    for cccccc in CCCCCC:
        if cccccc in area:
            return "인천서구"

    DDDDDD = ["인천광역시 미추홀구", "인천광역시 남구", "인천 남구", "인천시 미추홀구", "인천 미추홀구"]
    for dddddd in DDDDDD:
        if dddddd in area:
            return "인천미추홀구"
    
    EEEEEE = ["인천광역시 연수구", "인천시 연수구", "인천 연수구"]
    for eeeeee in EEEEEE:
        if eeeeee in area:
            return "인천연수구"

    FFFFFF = ["인천광역시 남동구", "인천시 남동구", "인천 남동구"]
    for ffffff in FFFFFF:
        if ffffff in area:
            return "인천남동구"
    
    GGGGGG = ["인천광역시 부평구", "인천시 부평구", "인천 부평구"]
    for gggggg in GGGGGG:
        if gggggg in area:
            return "인천부평구"
 
    HHHHHH = ["인천광역시 계양구", "인천시 계양구", "인천 계양구"]
    for hhhhhh in HHHHHH:
        if hhhhhh in area:
            return "인천계양구"
    
    IIIIII = ["인천광역시 강화군", "인천시 강화군", "인천 강화군"]
    for iiiiii in IIIIII:
        if iiiiii in area:
            return "인천강화군"

######울산#################################################################
    AAAAAAA = ["울산광역시 동구", "울산시 동구", "울산 동구"]
    for aaaaaaa in AAAAAAA:
        if aaaaaaa in area:
            return "울산동구"

    BBBBBBB = ["울산광역시 중구", "울산시 중구", "울산 중구"]
    for bbbbbbb in BBBBBBB:
        if bbbbbbb in area:
            return "울산중구"

    CCCCCCC = ["울산광역시 남구", "울산시 남구", "울산 남구"]
    for ccccccc in CCCCCCC:
        if ccccccc in area:
            return "울산남구"

    DDDDDDD = ["울산광역시 북구", "울산시 북구", "울산 북구"]
    for ddddddd in DDDDDDD:
        if ddddddd in area:
            return "울산북구"
    
    EEEEEEE = ["울산광역시 울주군", "울산시 울주군", "울산 울주군"]
    for eeeeeee in EEEEEEE:
        if eeeeeee in area:
            return "울산울주군"


######부산#################################################################3
    Ai = ["부산광역시 중구", "부산시 중구", "부산 중구"]
    for ai in Ai:
        if ai in area:
            return "부산중구"

    Bi = ["부산광역시 서구", "부산시 서구", "부산 서구"]
    for bi in Bi:
        if bi in area:
            return "부산서구"

    Ci = ["부산광역시 동구", "부산시 동구", "부산 동구"]
    for ci in Ci:
        if ci in area:
            return "부산동구"

    Di = ["부산광역시 영도구", "부산시 영도구", "부산 영도구"]
    for di in Di:
        if di in area:
            return "부산영도구"
    
    Ei = ["부산광역시 부산진구", "부산시 부산진구", "부산 부산진구"]
    for ei in Ei:
        if ei in area:
            return "부산부산진구"

    Fi = ["부산광역시 동래구", "부산시 동래구", "부산 동래구"]
    for fi in Fi:
        if fi in area:
            return "부산동래구"
    
    Gi = ["부산광역시 남구", "부산시 남구", "부산 남구"]
    for gi in Gi:
        if gi in area:
            return "부산남구"
 
    Hi = ["부산광역시 북구", "부산시 북구", "부산 북구"]
    for hi in Hi:
        if hi in area:
            return "부산북구"

    Ii = ["부산광역시 해운대구", "부산시 해운대구", "부산 해운대구"]
    for ii in Ii:
        if ii in area:
            return "부산해운대구"

    Ji = ["부산광역시 사하구", "부산시 사하구", "부산 사하구"]
    for ji in Ji:
        if ji in area:
            return "부산사하구"

    Ki = ["부산광역시 금정구", "부산시 금정구", "부산 금정구"]
    for ki in Ki:
        if ki in area:
            return "부산금정구"

    Li = ["부산광역시 강서구", "부산시 강서구", "부산 강서구"]
    for li in Li:
        if li in area:
            return "부산강서구"

    Mi = ["부산광역시 연제구", "부산시 연제구", "부산 연제구"]
    for mi in Mi:
        if mi in area:
            return "부산연제구"

    Ni = ["부산광역시 수영구", "부산시 수영구", "부산 수영구"]
    for ni in Ni:
        if ni in area:
            return "부산수영구"

    Oi = ["부산광역시 사상구", "부산시 사상구", "부산 사상구"]
    for oi in Oi:
        if oi in area:
            return "부산사상구"

    Pi = ["부산광역시 기장군", "부산시 기장군", "부산 기장군"]
    for pi in Pi:
        if pi in area:
            return "부산기장군"
        
######강원#################################################################3
    Aj = ["강원도 춘천시", "강원 춘천시"]
    for aj in Aj:
        if aj in area:
            return "강원춘천시"

    Bj = ["강원도 원주시", "강원 원주시"]
    for bj in Bj:
        if bj in area:
            return "강원원주시"

    Cj = ["강원도 강릉시", "강원 강릉시"]
    for cj in Cj:
        if cj in area:
            return "강원강릉시"

    Dj = ["강원도 동해시", "강원 동해시"]
    for dj in Dj:
        if dj in area:
            return "강원동해시"
    
    Ej = ["강원도 태백시", "강원 태백시"]
    for ej in Ej:
        if ej in area:
            return "강원태백시"

    Fj = ["강원도 속초시", "강원 속초시"]
    for fj in Fj:
        if fj in area:
            return "강원속초시"
    
    Gj = ["강원도 삼척시", "강원 삼척시"]
    for gj in Gj:
        if gj in area:
            return "강원삼척시"
 
    Hj = ["강원도 홍천군", "강원 홍천군"]
    for hj in Hj:
        if hj in area:
            return "강원홍천군"

    Ij = ["강원도 횡성군", "강원 횡성군"]
    for ij in Ij:
        if ij in area:
            return "강원횡성군"

    Jj = ["강원도 평창군", "강원 평창군"]
    for jj in Jj:
        if jj in area:
            return "강원평창군"

    Kj = ["강원도 정선군", "강원 정선군"]
    for kj in Kj:
        if kj in area:
            return "강원정선군"

    Lj = ["강원도 철원군", "강원 철원군"]
    for lj in Lj:
        if lj in area:
            return "강원철원군"

    Mj = ["강원도 화천군", "강원 화천군"]
    for mj in Mj:
        if mj in area:
            return "강원화천군"

    Nj = ["강원도 양구군", "강원 양구군"]
    for nj in Nj:
        if nj in area:
            return "강원양구군"

    Oj = ["강원도 인제군", "강원 인제군"]
    for oj in Oj:
        if oj in area:
            return "강원인제군"

    Pj = ["강원도 고성군", "강원 고성군"]
    for pj in Pj:
        if pj in area:
            return "강원고성군"

    Qj = ["강원도 영월군", "강원 영월군"]
    for qj in Qj:
        if qj in area:
            return "강원영월군"

    Rj = ["강원도 양양군", "강원 양양군"]
    for rj in Rj:
        if rj in area:
            return "강원양양군"
        
######전라남도#################################################################3
    Ap = ["전라남도 목포시", "전남 목포시"]
    for ap in Ap:
        if ap in area:
            return "전남목포시"

    Bp = ["전라남도 여수시", "전남 여수시"]
    for bp in Bp:
        if bp in area:
            return "전남여수시"

    Cp = ["전라남도 순천시", "전남 순천시"]
    for cp in Cp:
        if cp in area:
            return "전남순천시"

    Dp = ["전라남도 나주시", "전남 나주시"]
    for dp in Dp:
        if dp in area:
            return "전남나주시"
    
    Ep = ["전라남도 광양시", "전남 광양시"]
    for ep in Ep:
        if ep in area:
            return "전남광양시"

    Fp = ["전라남도 담양군", "전남 담양군"]
    for fp in Fp:
        if fp in area:
            return "전남담양군"
    
    Gp = ["전라남도 곡성군", "전남 곡성군"]
    for gp in Gp:
        if gp in area:
            return "전남곡성군"
 
    Hp = ["전라남도 구례군", "전남 구례군"]
    for hp in Hp:
        if hp in area:
            return "전남구례군"

    Ip = ["전라남도 고흥군", "전남 고흥군"]
    for ip in Ip:
        if ip in area:
            return "전남고흥군"

    Jp = ["전라남도 보성군", "전남 보성군"]
    for jp in Jp:
        if jp in area:
            return "전남보성군"

    Kp = ["전라남도 화순군", "전남 화순군"]
    for kp in Kp:
        if kp in area:
            return "전남화순군"

    Lp = ["전라남도 강진군", "전남 강진군"]
    for lp in Lp:
        if lp in area:
            return "전남강진군"

    Mp = ["전라남도 해남군", "전남 해남군"]
    for mp in Mp:
        if mp in area:
            return "전남해남군"

    Np = ["전라남도 영암군", "전남 영암군"]
    for np in Np:
        if np in area:
            return "전남영암군"

    Op = ["전라남도 무안군", "전남 무안군"]
    for op in Op:
        if op in area:
            return "전남무안군"

    Pp = ["전라남도 함평군", "전남 함평군"]
    for pp in Pp:
        if pp in area:
            return "전남함평군"

    Qp = ["전라남도 영광군", "전남 영광군"]
    for qp in Qp:
        if qp in area:
            return "전남영광군"

    Rp = ["전라남도 장성군", "전남 장성군"]
    for rp in Rp:
        if rp in area:
            return "전남장성군"

    Sp = ["전라남도 완도군", "전남 완도군"]
    for sp in Sp:
        if sp in area:
            return "전남완도군"

    Tp = ["전라남도 진도군", "전남 진도군"]
    for tp in Tp:
        if tp in area:
            return "전남진도군"

    Up = ["전라남도 신안군", "전남 신안군"]
    for up in Up:
        if up in area:
            return "전남신안군"

    Vp = ["전라남도 장흥군", "전남 장흥군"]
    for vp in Vp:
        if vp in area:
            return "전남장흥군"

######전라북도#################################################################3
    Aqq = ["전라북도 전주시 완산구", "전북 전주시 완산구"]
    for aqq in Aqq:
        if aqq in area:
            return "전북전주시완산구"

    Bqq = ["전라북도 전주시 덕진구", "전북 전주시 덕진구"]
    for bqq in Bqq:
        if bqq in area:
            return "전북전주시덕진구"

    Cqq = ["전라북도 군산시", "전북 군산시"]
    for cqq in Cqq:
        if cqq in area:
            return "전북군산시"

    Dqq = ["전라북도 익산시", "전북 익산시"]
    for dqq in Dqq:
        if dqq in area:
            return "전북익산시"
    
    Eqq = ["전라북도 정읍시", "전북 정읍시"]
    for eqq in Eqq:
        if eqq in area:
            return "전북정읍시"

    Fqq = ["전라북도 남원시", "전북 남원시"]
    for fqq in Fqq:
        if fqq in area:
            return "전북남원시"
    
    Gqq = ["전라북도 김제시", "전북 김제시"]
    for gqq in Gqq:
        if gqq in area:
            return "전북김제시"
 
    Hqq = ["전라북도 완주군", "전북 완주군"]
    for hqq in Hqq:
        if hqq in area:
            return "전북완주군"

    Iqq = ["전라북도 진안군", "전북 진안군"]
    for iqq in Iqq:
        if iqq in area:
            return "전북진안군"

    Jqq = ["전라북도 무주군", "전북 무주군"]
    for jqq in Jqq:
        if jqq in area:
            return "전북무주군"

    Kqq = ["전라북도 장수군", "전북 장수군"]
    for kqq in Kqq:
        if kqq in area:
            return "전북장수군"

    Lqq = ["전라북도 임실군", "전북 임실군"]
    for lqq in Lqq:
        if lqq in area:
            return "전북임실군"

    Mqq = ["전라북도 순창군", "전북 순창군"]
    for mqq in Mqq:
        if mqq in area:
            return "전북순창군"

    Nqq = ["전라북도 고창군", "전북 고창군"]
    for nqq in Nqq:
        if nqq in area:
            return "전북고창군"

    Oqq = ["전라북도 무안군", "전북 무안군"]
    for oqq in Oqq:
        if oqq in area:
            return "전북무안군"

######충청남도#################################################################3
    Aw = ["충청남도 천안시 동남구", "충남 천안시 동남구"]
    for aw in Aw:
        if aw in area:
            return "충남천안시동남구"

    Bw = ["충청남도 천안시 서북구", "충남 천안시 서북구"]
    for bw in Bw:
        if bw in area:
            return "충남천안시서북구"

    Cw = ["충청남도 공주시", "충남 공주시"]
    for cw in Cw:
        if cw in area:
            return "충남공주시"

    Dw = ["충청남도 보령시", "충남 보령시"]
    for dw in Dw:
        if dw in area:
            return "충남보령시"
    
    Ew = ["충청남도 아산시", "충남 아산시"]
    for ew in Ew:
        if ew in area:
            return "충남아산시"

    Fw = ["충청남도 서산시", "충남 서산시"]
    for fw in Fw:
        if fw in area:
            return "충남서산시"
    
    Gw = ["충청남도 논산시", "충남 논산시"]
    for gw in Gw:
        if gw in area:
            return "충남논산시"
 
    Hw = ["충청남도 계룡시", "충남 계룡시"]
    for hw in Hw:
        if hw in area:
            return "충남계룡시"

    Iw = ["충청남도 당진시", "충남 당진시"]
    for iw in Iw:
        if iw in area:
            return "충남당진시"

    Jw = ["충청남도 금산군", "충남 금산군"]
    for jw in Jw:
        if jw in area:
            return "충남금산군"

    Kw = ["충청남도 부여군", "충남 부여군"]
    for kw in Kw:
        if kw in area:
            return "충남부여군"

    Lw = ["충청남도 서천군", "충남 서천군"]
    for lw in Lw:
        if lw in area:
            return "충남서천군"

    Mw = ["충청남도 청양군", "충남 청양군"]
    for mw in Mw:
        if mw in area:
            return "충남청양군"

    Nw = ["충청남도 홍성군", "충남 홍성군"]
    for nw in Nw:
        if nw in area:
            return "충남홍성군"

    Ow = ["충청남도 예산군", "충남 예산군"]
    for ow in Ow:
        if ow in area:
            return "충남예산군"

    Pw = ["충청남도 태안군", "충남 태안군"]
    for pw in Pw:
        if pw in area:
            return "충남태안군"

######충청북도#################################################################3
    Aqq = ["충청북도 청주시 상당구", "충북 청주시 상당구"]
    for aqq in Aqq:
        if aqq in area:
            return "충북청주시상당구"

    Bqq = ["충청북도 청주시 서원구", "충북 청주시 서원구"]
    for bqq in Bqq:
        if bqq in area:
            return "충북청주시서원구"

    Cqq = ["충청북도 청주시 흥덕구", "충북 청주시 흥덕구"]
    for cqq in Cqq:
        if cqq in area:
            return "충북청주시흥덕구"

    Dqq = ["충청북도 청주시 청원구", "충북 청주시 청원구"]
    for dqq in Dqq:
        if dqq in area:
            return "충북청주시청원구"
    
    Eqq = ["충청북도 충주시", "충북 충주시"]
    for eqq in Eqq:
        if eqq in area:
            return "충북충주시"

    Fqq = ["충청북도 제천시", "충북 제천시"]
    for fqq in Fqq:
        if fqq in area:
            return "충북제천시"
    
    Gqq = ["충청북도 보은군", "충북 보은군"]
    for gqq in Gqq:
        if gqq in area:
            return "충북보은군"
 
    Hqq = ["충청북도 옥천군", "충북 옥천군"]
    for hqq in Hqq:
        if hqq in area:
            return "충북옥천군"

    Iqq = ["충청북도 영동군", "충북 영동군"]
    for iqq in Iqq:
        if iqq in area:
            return "충북영동군"

    Jqq = ["충청북도 증평군", "충북 증평군"]
    for jqq in Jqq:
        if jqq in area:
            return "충북증평군"

    Kqq = ["충청북도 진천군", "충북 진천군"]
    for kqq in Kqq:
        if kqq in area:
            return "충북진천군"

    Lqq = ["충청북도 괴산군", "충북 괴산군"]
    for lqq in Lqq:
        if lqq in area:
            return "충북괴산군"

    Mqq = ["충청북도 음성군", "충북 음성군"]
    for mqq in Mqq:
        if mqq in area:
            return "충북음성군"

    Nqq = ["충청북도 단양군", "충북 단양군"]
    for nqq in Nqq:
        if nqq in area:
            return "충북단양군"

######경상남도#################################################################3
    Aei = ["경상남도 창원시 의창구", "경남 창원시 의창구"]
    for aei in Aei:
        if aei in area:
            return "경남창원시의창구"

    Bei = ["경상남도 창원시 성산구", "경남 창원시 성산구"]
    for bei in Bei:
        if bei in area:
            return "경남창원시성산구"

    Cei = ["경상남도 창원시 마산합포구", "경남 창원시 마산합포구"]
    for cei in Cei:
        if cei in area:
            return "경남창원시마산합포구"

    Dei = ["경상남도 창원시 마산회원구", "경남 창원시 마산회원구"]
    for dei in Dei:
        if dei in area:
            return "경남창원시마산회원구"
    
    Eei = ["경상남도 창원시 진해구", "경남 창원시 진해구"]
    for eei in Eei:
        if eei in area:
            return "경남창원시진해구"

    Fei = ["경상남도 진주시", "경남 진주시"]
    for fei in Fei:
        if fei in area:
            return "경남진주시"
    
    Gei = ["경상남도 거제시", "경남 거제시"]
    for gei in Gei:
        if gei in area:
            return "경남거제시"
 
    Hei = ["경상남도 양산시", "경남 양산시"]
    for hei in Hei:
        if hei in area:
            return "경남양산시"

    Iei = ["경상남도 의령군", "경남 의령군"]
    for iei in Iei:
        if iei in area:
            return "경남의령군"

    Jei = ["경상남도 함안군", "경남 함안군"]
    for jei in Jei:
        if jei in area:
            return "경남함안군"

    Kei = ["경상남도 창녕군", "경남 창녕군"]
    for kei in Kei:
        if kei in area:
            return "경남창녕군"

    Lei = ["경상남도 고성군", "경남 고성군"]
    for lei in Lei:
        if lei in area:
            return "경남고성군"

    Mei = ["경상남도 통영시", "경남 통영시"]
    for mei in Mei:
        if mei in area:
            return "경남통영시"

    Nei = ["경상남도 사천시", "경남 사천시"]
    for nei in Nei:
        if nei in area:
            return "경남사천시"

    Oei = ["경상남도 김해시", "경남 김해시"]
    for oei in Oei:
        if oei in area:
            return "경남김해시"

    Pei = ["경상남도 밀양시", "경남 밀양시"]
    for pei in Pei:
        if pei in area:
            return "경남밀양시"

    Qei = ["경상남도 합천군", "경남 합천군"]
    for qei in Qei:
        if qei in area:
            return "경남합천군"

    Rei = ["경상남도 남해군", "경남 남해군"]
    for rei in Rei:
        if rei in area:
            return "경남남해군"

    Sei = ["경상남도 하동군", "경남 하동군"]
    for sei in Sei:
        if sei in area:
            return "경남하동군"

    Tei = ["경상남도 산청군", "경남 산청군"]
    for tei in Tei:
        if tei in area:
            return "경남산청군"

    Uei = ["경상남도 함양군", "경남 함양군"]
    for uei in Uei:
        if uei in area:
            return "경남함양군"

    Vei = ["경상남도 거창군", "경남 거창군"]
    for vei in Vei:
        if vei in area:
            return "경남거창군"

######경상북도#################################################################3
    Axi = ["경상북도 포항시 남구", "경북 포항시 남구"]
    for axi in Axi:
        if axi in area:
            return "경북포항시남구"

    Bxi = ["경상북도 포항시 북구", "경북 포항시 북구"]
    for bxi in Bxi:
        if bxi in area:
            return "경북포항시북구"

    Cxi = ["경상북도 경주시", "경북 경주시"]
    for cxi in Cxi:
        if cxi in area:
            return "경북경주시"

    Dxi = ["경상북도 김천시", "경북 김천시"]
    for dxi in Dxi:
        if dxi in area:
            return "경북김천시"
    
    Exi = ["경상북도 안동시", "경북 안동시"]
    for exi in Exi:
        if exi in area:
            return "경북안동시"

    Fxi = ["경상북도 구미시", "경북 구미시"]
    for fxi in Fxi:
        if fxi in area:
            return "경북구미시"
    
    Gxi = ["경상북도 의성군", "경북 의성군"]
    for gxi in Gxi:
        if gxi in area:
            return "경북의성군"
 
    Hxi = ["경상북도 청송군", "경북 청송군"]
    for hxi in Hxi:
        if hxi in area:
            return "경북청송군"

    Ixi = ["경상북도 영양군", "경북 영양군"]
    for ixi in Ixi:
        if ixi in area:
            return "경북영양군"

    Jxi = ["경상북도 영덕군", "경북 영덕군"]
    for jxi in Jxi:
        if jxi in area:
            return "경북영덕군"

    Kxi = ["경상북도 청도군", "경북 청도군"]
    for kxi in Kxi:
        if kxi in area:
            return "경북청도군"

    Lxi = ["경상북도 고령군", "경북 고령군"]
    for lxi in Lxi:
        if lxi in area:
            return "경북고령군"

    Mxi = ["경상북도 영주시", "경북 영주시"]
    for mxi in Mxi:
        if mxi in area:
            return "경북영주시"

    Nxi = ["경상북도 영천시", "경북 영천시"]
    for nxi in Nxi:
        if nxi in area:
            return "경북영천시"

    Oxi = ["경상북도 상주시", "경북 상주시"]
    for oxi in Oxi:
        if oxi in area:
            return "경북상주시"

    Pxi = ["경상북도 문경시", "경북 문경시"]
    for pxi in Pxi:
        if pxi in area:
            return "경북문경시"

    Qxi = ["경상북도 경산시", "경북 경산시"]
    for qxi in Qxi:
        if qxi in area:
            return "경북경산시"

    Rxi = ["경상북도 군위군", "경북 군위군"]
    for rxi in Rxi:
        if rxi in area:
            return "경북군위군"

    Sxi = ["경상북도 성주군", "경북 성주군"]
    for sxi in Sxi:
        if sxi in area:
            return "경북성주군"

    Txi = ["경상북도 칠곡군", "경북 칠곡군"]
    for txi in Txi:
        if txi in area:
            return "경북칠곡군"

    Uxi = ["경상북도 예천군", "경북 예천군"]
    for uxi in Uxi:
        if uxi in area:
            return "경북예천군"

    Vxi = ["경상북도 봉화군", "경북 봉화군"]
    for vxi in Vxi:
        if vxi in area:
            return "경북봉화군"

    Vxi = ["경상북도 울진군", "경북 울진군"]
    for vxi in Vxi:
        if vxi in area:
            return "경북울진군"
    
    Xxi = ["경상북도 울릉군", "경북 울릉군"]
    for xxi in Xxi:
        if xxi in area:
            return "경북울릉군"
        
######경기도#################################################################3
    Ayi = ["경기도 수원시 장안구", "경기 수원시 장안구"]
    for ayi in Ayi:
        if ayi in area:
            return "경기수원시장안구"

    Byi = ["경기도 수원시 권선구", "경기 수원시 권선구"]
    for byi in Byi:
        if byi in area:
            return "경기수원시권선구"

    Cyi = ["경기도 수원시 팔달구", "경기 수원시 팔달구"]
    for cyi in Cyi:
        if cyi in area:
            return "경기수원시팔달구"

    Dyi = ["경기도 수원시 영통구", "경기 수원시 영통구"]
    for dyi in Dyi:
        if dyi in area:
            return "경기수원시영통구"
    
    Eyi = ["경기도 성남시 수정구", "경기 성남시 수정구"]
    for eyi in Eyi:
        if eyi in area:
            return "경기성남시수정구"

    Fyi = ["경기도 성남시 중원구", "경기 성남시 중원구"]
    for fyi in Fyi:
        if fyi in area:
            return "경기성남시중원구"
    
    Gyi = ["경기도 성남시 분당구", "경기 성남시 분당구"]
    for gyi in Gyi:
        if gyi in area:
            return "경기성남시분당구"
 
    Hyi = ["경기도 고양시 덕양구", "경기 고양시 덕양구"]
    for hyi in Hyi:
        if hyi in area:
            return "경기고양시덕양구"

    Iyi = ["경기도 고양시 일산동구", "경기 고양시 일산동구"]
    for iyi in Iyi:
        if iyi in area:
            return "경기고양시일산동구"

    Jyi = ["경기도 고양시 일산서구", "경기 고양시 일산서구"]
    for jyi in Jyi:
        if jyi in area:
            return "경기고양시일산서구"

    Kyi = ["경기도 과천시", "경기 과천시"]
    for kyi in Kyi:
        if kyi in area:
            return "경기과천시"

    Lyi = ["경기도 구리시", "경기 구리시"]
    for lyi in Lyi:
        if lyi in area:
            return "경기구리시"

    Myi = ["경기도 남양주시", "경기 남양주시"]
    for myi in Myi:
        if myi in area:
            return "경기남양주시"

    Nyi = ["경기도 오산시", "경기 오산시"]
    for nyi in Nyi:
        if nyi in area:
            return "경기오산시"

    Oyi = ["경기도 의정부시", "경기 의정부시"]
    for oyi in Oyi:
        if oyi in area:
            return "경기의정부시"

    Pyi = ["경기도 안양시 만안구", "경기 안양시 만안구"]
    for pyi in Pyi:
        if pyi in area:
            return "경기안양시만안구"

    Qyi = ["경기도 안양시 동안구", "경기 안양시 동안구"]
    for qyi in Qyi:
        if qyi in area:
            return "경기안양시동안구"

    Ryi = ["경기도 부천시", "경기 부천시"]
    for ryi in Ryi:
        if ryi in area:
            return "경기부천시"

    Syi = ["경기도 광명시", "경기 광명시"]
    for syi in Syi:
        if syi in area:
            return "경기광명시"

    Tyi = ["경기도 평택시", "경기 평택시"]
    for tyi in Tyi:
        if tyi in area:
            return "경기평택시"

    Uyi = ["경기도 동두천시", "경기 동두천시"]
    for uyi in Uyi:
        if uyi in area:
            return "경기동두천시"

    Vyi = ["경기도 시흥시", "경기 시흥시"]
    for vyi in Vyi:
        if vyi in area:
            return "경기시흥시"

    Vyi = ["경기도 군포시", "경기 군포시"]
    for vyi in Vyi:
        if vyi in area:
            return "경기군포시"
    
    Xyi = ["경기도 의왕시", "경기 의왕시"]
    for xyi in Xyi:
        if xyi in area:
            return "경기의왕시"

    Yyi = ["경기도 하남시", "경기 하남시"]
    for yyi in Yyi:
        if yyi in area:
            return "경기하남시"
    
    Zyi = ["경기도 용인시 처인구", "경기 용인시 처인구"]
    for zyi in Zyi:
        if zyi in area:
            return "경기용인시처인구"

    AAyi = ["경기도 용인시 기흥구", "경기 용인시 기흥구"]
    for aayi in AAyi:
        if aayi in area:
            return "경기용인시기흥구"

    BByi = ["경기도 용인시 수지구", "경기 용인시 수지구"]
    for bbyi in BByi:
        if bbyi in area:
            return "경기용인시수지구"

    CCyi = ["경기도 가평군", "경기 가평군"]
    for ccyi in CCyi:
        if ccyi in area:
            return "경기가평군"

    DDyi = ["경기도 연천군", "경기 연천군"]
    for ddyi in DDyi:
        if ddyi in area:
            return "경기연천군"
    
    EEyi = ["경기도 여주시", "경기 여주시"]
    for eeyi in EEyi:
        if eeyi in area:
            return "경기여주시"

    FFyi = ["경기도 포천시", "경기 포천시"]
    for ffyi in FFyi:
        if ffyi in area:
            return "경기포천시"
    
    GGyi = ["경기도 양주시", "경기 양주시"]
    for ggyi in GGyi:
        if ggyi in area:
            return "경기양주시"
 
    HHyi = ["경기도 광주시", "경기 광주시"]
    for hhyi in HHyi:
        if hhyi in area:
            return "경기광주시"

    IIyi = ["경기도 화성시", "경기 화성시"]
    for iiyi in IIyi:
        if iiyi in area:
            return "경기화성시"

    JJyi = ["경기도 안산시 상록구", "경기 안산시 상록구"]
    for jjyi in JJyi:
        if jjyi in area:
            return "경기안산시 상록구"

    KKyi = ["경기도 안산시 단원구", "경기 안산시 단원구"]
    for kkyi in KKyi:
        if kkyi in area:
            return "경기안산시 단원구"

    LLyi = ["경기도 파주시", "경기 파주시"]
    for llyi in LLyi:
        if llyi in area:
            return "경기파주시"

    MMyi = ["경기도 이천시", "경기 이천시"]
    for mmyi in MMyi:
        if mmyi in area:
            return "경기이천시"

    NNyi = ["경기도 김포시", "경기 김포시"]
    for nnyi in NNyi:
        if nnyi in area:
            return "경기김포시"

    OOyi = ["경기도 안성시", "경기 안성시"]
    for ooyi in OOyi:
        if ooyi in area:
            return "경기안성시"


# df["area_cate"] = df["area"].apply(lambda area: area_category(area))
# # # # print(df)
# # # # print(df.head(60))
# data["stores"] = df
# print(df.tail(50))

