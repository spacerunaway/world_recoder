import sys
sys.path.append('../music')
from chord import *
""" C Chords"""
# C basic
CM = Major_Triad(do)
Cm = Minor_Triad(do)
Caug = Aug_Triad(do)
Cdim = Dim_Triad(do)
# C Major
CM7 = CM.major_seventh()
CM6 = CM.sixth()
Cdom7 = CM.dominant_seventh()
Cdom9 = CM.dominant_ninth()
Cdom11 = CM.dominant_eleventh()
Cdom13 = CM.dominant_thirteenth()
Cadd9 = CM.add(['M9'])
C7add9 = Cdom7.add(['M9'])
CM7add9 = CM7.add(['M9'])
Cadd11 = CM.add(['P11'])
C69 = CM.add(['M6','M9'])
Csus2 = CM.sus2()
Csus4 = CM.sus4()
C7sus4 = Cdom7.sus4()
# C minor
Cm7 = Cm.seventh()
CmM7 = Cm.major_seventh()
Cm6 = Cm.sixth()
Cmb5 = Cm.b5()
Cm7b5 = Cm.seventh_b5()
# C augmented
Caug7 = Caug.seventh()
CaugM7 = Caug.major_seventh()
# C diminished
Cdim7 = Cdim.seventh()
Chalfdim7 = Cdim.half_seventh()
""" D Chords"""
# D basic
DM = Major_Triad(re)
Dm = Minor_Triad(re)
Daug = Aug_Triad(re)
Ddim = Dim_Triad(re)
# D Major
DM7 = DM.major_seventh()
DM6 = DM.sixth()
Ddom7 = DM.dominant_seventh()
Ddom9 = DM.dominant_ninth()
Ddom11 = DM.dominant_eleventh()
Ddom13 = DM.dominant_thirteenth()
Dadd9 = DM.add(['M9'])
D7add9 = Ddom7.add(['M9'])
DM7add9 = DM7.add(['M9'])
Dadd11 = DM.add(['P11'])
D69 = DM.add(['M6','M9'])
Dsus2 = DM.sus2()
Dsus4 = DM.sus4()
D7sus4 = Ddom7.sus4()
# D minor
Dm7 = Dm.seventh()
DmM7 = Dm.major_seventh()
Dm6 = Dm.sixth()
Dmb5 = Dm.b5()
Dm7b5 = Dm.seventh_b5()
# D augmented
Daug7 = Daug.seventh()
DaugM7 = Daug.major_seventh()
# D diminished
Ddim7 = Ddim.seventh()
Dhalfdim7 = Ddim.half_seventh()
""" E Chords"""
# E basic
EM = Major_Triad(mi)
Em = Minor_Triad(mi)
Eaug = Aug_Triad(mi)
Edim = Dim_Triad(mi)
# E Major
EM7 = EM.major_seventh()
EM6 = EM.sixth()
Edom7 = EM.dominant_seventh()
Edom9 = EM.dominant_ninth()
Edom11 = EM.dominant_eleventh()
Edom13 = EM.dominant_thirteenth()
Eadd9 = EM.add(['M9'])
E7add9 = Edom7.add(['M9'])
EM7add9 = EM7.add(['M9'])
Eadd11 = EM.add(['P11'])
E69 = EM.add(['M6','M9'])
Esus2 = EM.sus2()
Esus4 = EM.sus4()
E7sus4 = Edom7.sus4()
# E minor
Em7 = Em.seventh()
EmM7 = Em.major_seventh()
Em6 = Em.sixth()
Emb5 = Em.b5()
Em7b5 = Em.seventh_b5()
# E augmented
Eaug7 = Eaug.seventh()
EaugM7 = Eaug.major_seventh()
# E diminished
Edim7 = Edim.seventh()
Ehalfdim7 = Edim.half_seventh()
""" F Chords"""
# F basic
FM = Major_Triad(fa)
Fm = Minor_Triad(fa)
Faug = Aug_Triad(fa)
Fdim = Dim_Triad(fa)
# F Major
FM7 = FM.major_seventh()
FM6 = FM.sixth()
Fdom7 = FM.dominant_seventh()
Fdom9 = FM.dominant_ninth()
Fdom11 = FM.dominant_eleventh()
Fdom13 = FM.dominant_thirteenth()
Fadd9 = FM.add(['M9'])
F7add9 = Fdom7.add(['M9'])
FM7add9 = FM7.add(['M9'])
Fadd11 = FM.add(['P11'])
F69 = FM.add(['M6','M9'])
Fsus2 = FM.sus2()
Fsus4 = FM.sus4()
F7sus4 = Fdom7.sus4()
# F minor
Fm7 = Fm.seventh()
FmM7 = Fm.major_seventh()
Fm6 = Fm.sixth()
Fmb5 = Fm.b5()
Fm7b5 = Fm.seventh_b5()
# F augmented
Faug7 = Faug.seventh()
FaugM7 = Faug.major_seventh()
# F diminished
Fdim7 = Fdim.seventh()
Fhalfdim7 = Fdim.half_seventh()
""" G Chords"""
# G basic
GM = Major_Triad(so)
Gm = Minor_Triad(so)
Gaug = Aug_Triad(so)
Gdim = Dim_Triad(so)
# G Major
GM7 = GM.major_seventh()
GM6 = GM.sixth()
Gdom7 = GM.dominant_seventh()
Gdom9 = GM.dominant_ninth()
Adom11 = GM.dominant_eleventh()
Adom13 = GM.dominant_thirteenth()
Gadd9 = GM.add(['M9'])
G7add9 = Gdom7.add(['M9'])
GM7add9 = GM7.add(['M9'])
Gadd11 = GM.add(['P11'])
G69 = GM.add(['M6','M9'])
Gsus2 = GM.sus2()
Gsus4 = GM.sus4()
G7sus4 = Gdom7.sus4()
# G minor
Gm7 = Gm.seventh()
GmM7 = Gm.major_seventh()
Gm6 = Gm.sixth()
Gmb5 = Gm.b5()
Gm7b5 = Gm.seventh_b5()
# G augmented
Gaug7 = Gaug.seventh()
GaugM7 = Gaug.major_seventh()
# G diminished
Gdim7 = Gdim.seventh()
Ghalfdim7 = Gdim.half_seventh()
""" A Chords"""
# A basic
AM = Major_Triad(la)
Am = Minor_Triad(la)
Aaug = Aug_Triad(la)
Adim = Dim_Triad(la)
# A Major
AM7 = AM.major_seventh()
AM6 = AM.sixth()
Adom7 = AM.dominant_seventh()
Adom9 = AM.dominant_ninth()
Gdom11 = AM.dominant_eleventh()
Gdom13 = AM.dominant_thirteenth()
Aadd9 = AM.add(['M9'])
A7add9 = Adom7.add(['M9'])
AM7add9 = AM7.add(['M9'])
Aadd11 = AM.add(['P11'])
A69 = AM.add(['M6','M9'])
Asus2 = AM.sus2()
Asus4 = AM.sus4()
A7sus4 = Adom7.sus4()
# A minor
Am7 = Am.seventh()
AmM7 = Am.major_seventh()
Am6 = Am.sixth()
Amb5 = Am.b5()
Am7b5 = Am.seventh_b5()
# A augmented
Aaug7 = Aaug.seventh()
AaugM7 = Aaug.major_seventh()
# A diminished
Adim7 = Adim.seventh()
Ahalfdim7 = Adim.half_seventh()
""" B Chords"""
# B basic
BM = Major_Triad(si)
Bm = Minor_Triad(si)
Baug = Aug_Triad(si)
Bdim = Dim_Triad(si)
# B Major
BM7 = BM.major_seventh()
BM6 = BM.sixth()
Bdom7 = BM.dominant_seventh()
Bdom9 = BM.dominant_ninth()
Bdom11 = BM.dominant_eleventh()
Bdom13 = BM.dominant_thirteenth()
Badd9 = BM.add(['M9'])
B7add9 = Bdom7.add(['M9'])
BM7add9 = BM7.add(['M9'])
Badd11 = BM.add(['P11'])
B69 = BM.add(['M6','M9'])
Bsus2 = BM.sus2()
Bsus4 = BM.sus4()
B7sus4 = Bdom7.sus4()
# B minor
Bm7 = Bm.seventh()
BmM7 = Bm.major_seventh()
Bm6 = Bm.sixth()
Bmb5 = Bm.b5()
Bm7b5 = Bm.seventh_b5()
# B augmented
Baug7 = Baug.seventh()
BaugM7 = Baug.major_seventh()
# B diminished
Bdim7 = Bdim.seventh()
Bhalfdim7 = Bdim.half_seventh()
""" Cb Chords"""
# Cb basic
CbM = Major_Triad(si)
Cbm = Minor_Triad(si)
Cbaug = Aug_Triad(si)
Cbdim = Dim_Triad(si)
# Cb Major
CbM7 = CbM.major_seventh()
CbM6 = CbM.sixth()
Cbdom7 = CbM.dominant_seventh()
Cbdom9 = CbM.dominant_ninth()
Cbdom11 = CbM.dominant_eleventh()
Cbdom13 = CbM.dominant_thirteenth()
Cbadd9 = CbM.add(['M9'])
Cb7add9 = Cbdom7.add(['M9'])
CbM7add9 = CbM7.add(['M9'])
Cbadd11 = CbM.add(['P11'])
Cb69 = CbM.add(['M6','M9'])
Cbsus2 = CbM.sus2()
Cbsus4 = CbM.sus4()
Cb7sus4 = Cbdom7.sus4()
# Cb minor
Cbm7 = Cbm.seventh()
CbmM7 = Cbm.major_seventh()
Cbm6 = Cbm.sixth()
Cbmb5 = Cbm.b5()
Cbm7b5 = Cbm.seventh_b5()
# Cb augmented
Cbaug7 = Cbaug.seventh()
CbaugM7 = Cbaug.major_seventh()
# Cb diminished
Cbdim7 = Cbdim.seventh()
Cbhalfdim7 = Cbdim.half_seventh()
""" Cs Chords"""
# Cs basic
CsM = Major_Triad(de)
Csm = Minor_Triad(de)
Csaug = Aug_Triad(de)
Csdim = Dim_Triad(de)
# Cs Major
CsM7 = CsM.major_seventh()
CsM6 = CsM.sixth()
Csdom7 = CsM.dominant_seventh()
Csdom9 = CsM.dominant_ninth()
Csdom11 = CsM.dominant_eleventh()
Csdom13 = CsM.dominant_thirteenth()
Csadd9 = CsM.add(['M9'])
Cs7add9 = Csdom7.add(['M9'])
CsM7add9 = CsM7.add(['M9'])
Csadd11 = CsM.add(['P11'])
Cs69 = CsM.add(['M6','M9'])
Cssus2 = CsM.sus2()
Cssus4 = CsM.sus4()
Cs7sus4 = Csdom7.sus4()
# Cs minor
Csm7 = Csm.seventh()
CsmM7 = Csm.major_seventh()
Csm6 = Csm.sixth()
Csmb5 = Csm.b5()
Csm7b5 = Csm.seventh_b5()
# Cs augmented
Csaug7 = Csaug.seventh()
CsaugM7 = Csaug.major_seventh()
# Cs diminished
Csdim7 = Csdim.seventh()
Cshalfdim7 = Csdim.half_seventh()
""" Db Chords"""
# Db basic
DbM = Major_Triad(de)
Dbm = Minor_Triad(de)
Dbaug = Aug_Triad(de)
Dbdim = Dim_Triad(de)
# Db Major
DbM7 = DbM.major_seventh()
DbM6 = DbM.sixth()
Dbdom7 = DbM.dominant_seventh()
Dbdom9 = DbM.dominant_ninth()
Dbdom11 = DbM.dominant_eleventh()
Dbdom13 = DbM.dominant_thirteenth()
Dbadd9 = DbM.add(['M9'])
Db7add9 = Dbdom7.add(['M9'])
DbM7add9 = DbM7.add(['M9'])
Dbadd11 = DbM.add(['P11'])
Db69 = DbM.add(['M6','M9'])
Dbsus2 = DbM.sus2()
Dbsus4 = DbM.sus4()
Db7sus4 = Dbdom7.sus4()
# Db minor
Dbm7 = Dbm.seventh()
DbmM7 = Dbm.major_seventh()
Dbm6 = Dbm.sixth()
Dbmb5 = Dbm.b5()
Dbm7b5 = Dbm.seventh_b5()
# Db augmented
Dbaug7 = Dbaug.seventh()
DbaugM7 = Dbaug.major_seventh()
# Db diminished
Dbdim7 = Dbdim.seventh()
Dbhalfdim7 = Dbdim.half_seventh()
""" Ds Chords"""
# Ds basic
DsM = Major_Triad(ri)
Dsm = Minor_Triad(ri)
Dsaug = Aug_Triad(ri)
Dsdim = Dim_Triad(ri)
# Ds Major
DsM7 = DsM.major_seventh()
DsM6 = DsM.sixth()
Dsdom7 = DsM.dominant_seventh()
Dsdom9 = DsM.dominant_ninth()
Dsdom11 = DsM.dominant_eleventh()
Dsdom13 = DsM.dominant_thirteenth()
Dsadd9 = DsM.add(['M9'])
Ds7add9 = Dsdom7.add(['M9'])
DsM7add9 = DsM7.add(['M9'])
Dsadd11 = DsM.add(['P11'])
Ds69 = DsM.add(['M6','M9'])
Dssus2 = DsM.sus2()
Dssus4 = DsM.sus4()
Ds7sus4 = Dsdom7.sus4()
# Ds minor
Dsm7 = Dsm.seventh()
DsmM7 = Dsm.major_seventh()
Dsm6 = Dsm.sixth()
Dsmb5 = Dsm.b5()
Dsm7b5 = Dsm.seventh_b5()
# Ds augmented
Dsaug7 = Dsaug.seventh()
DsaugM7 = Dsaug.major_seventh()
# Ds diminished
Dsdim7 = Dsdim.seventh()
Dshalfdim7 = Dsdim.half_seventh()
""" Eb Chords"""
# Eb basic
EbM = Major_Triad(ri)
Ebm = Minor_Triad(ri)
Ebaug = Aug_Triad(ri)
Ebdim = Dim_Triad(ri)
# Eb Major
EbM7 = EbM.major_seventh()
EbM6 = EbM.sixth()
Ebdom7 = EbM.dominant_seventh()
Ebdom9 = EbM.dominant_ninth()
Ebdom11 = EbM.dominant_eleventh()
Ebdom13 = EbM.dominant_thirteenth()
Ebadd9 = EbM.add(['M9'])
Eb7add9 = Ebdom7.add(['M9'])
EbM7add9 = EbM7.add(['M9'])
Ebadd11 = EbM.add(['P11'])
Eb69 = EbM.add(['M6','M9'])
Ebsus2 = EbM.sus2()
Ebsus4 = EbM.sus4()
Eb7sus4 = Ebdom7.sus4()
# Eb minor
Ebm7 = Ebm.seventh()
EbmM7 = Ebm.major_seventh()
Ebm6 = Ebm.sixth()
Ebmb5 = Ebm.b5()
Ebm7b5 = Ebm.seventh_b5()
# Eb augmented
Ebaug7 = Ebaug.seventh()
EbaugM7 = Ebaug.major_seventh()
# Eb diminished
Ebdim7 = Ebdim.seventh()
Ebhalfdim7 = Ebdim.half_seventh()
""" Es Chords"""
# Es basic
EsM = Major_Triad(fa)
Esm = Minor_Triad(fa)
Esaug = Aug_Triad(fa)
Esdim = Dim_Triad(fa)
# Es Major
EsM7 = EsM.major_seventh()
EsM6 = EsM.sixth()
Esdom7 = EsM.dominant_seventh()
Esdom9 = EsM.dominant_ninth()
Esdom11 = EsM.dominant_eleventh()
Esdom13 = EsM.dominant_thirteenth()
Esadd9 = EsM.add(['M9'])
Es7add9 = Esdom7.add(['M9'])
EsM7add9 = EsM7.add(['M9'])
Esadd11 = EsM.add(['P11'])
Es69 = EsM.add(['M6','M9'])
Essus2 = EsM.sus2()
Essus4 = EsM.sus4()
Es7sus4 = Esdom7.sus4()
# Es minor
Esm7 = Esm.seventh()
EsmM7 = Esm.major_seventh()
Esm6 = Esm.sixth()
Esmb5 = Esm.b5()
Esm7b5 = Esm.seventh_b5()
# Es augmented
Esaug7 = Esaug.seventh()
EsaugM7 = Esaug.major_seventh()
# Es diminished
Esdim7 = Esdim.seventh()
Eshalfdim7 = Esdim.half_seventh()
""" Fs Chords"""
# Fs basic
FsM = Major_Triad(fi)
Fsm = Minor_Triad(fi)
Fsaug = Aug_Triad(fi)
Fsdim = Dim_Triad(fi)
# Fs Major
FsM7 = FsM.major_seventh()
FsM6 = FsM.sixth()
Fsdom7 = FsM.dominant_seventh()
Fsdom9 = FsM.dominant_ninth()
Fsdom11 = FsM.dominant_eleventh()
Fsdom13 = FsM.dominant_thirteenth()
Fsadd9 = FsM.add(['M9'])
Fs7add9 = Fsdom7.add(['M9'])
FsM7add9 = FsM7.add(['M9'])
Fsadd11 = FsM.add(['P11'])
Fs69 = FsM.add(['M6','M9'])
Fssus2 = FsM.sus2()
Fssus4 = FsM.sus4()
Fs7sus4 = Fsdom7.sus4()
# Fs minor
Fsm7 = Fsm.seventh()
FsmM7 = Fsm.major_seventh()
Fsm6 = Fsm.sixth()
Fsmb5 = Fsm.b5()
Fsm7b5 = Fsm.seventh_b5()
# Fs augmented
Fsaug7 = Fsaug.seventh()
FsaugM7 = Fsaug.major_seventh()
# Fs diminished
Fsdim7 = Fsdim.seventh()
Fshalfdim7 = Fsdim.half_seventh()
""" Gb Chords"""
# Gb basic
GbM = Major_Triad(fi)
Gbm = Minor_Triad(fi)
Gbaug = Aug_Triad(fi)
Gbdim = Dim_Triad(fi)
# Gb Major
GbM7 = GbM.major_seventh()
GbM6 = GbM.sixth()
Gbdom7 = GbM.dominant_seventh()
Gbdom9 = GbM.dominant_ninth()
Gbdom11 = GbM.dominant_eleventh()
Gbdom13 = GbM.dominant_thirteenth()
Gbadd9 = GbM.add(['M9'])
Gb7add9 = Gbdom7.add(['M9'])
GbM7add9 = GbM7.add(['M9'])
Gbadd11 = GbM.add(['P11'])
Gb69 = GbM.add(['M6','M9'])
Gbsus2 = GbM.sus2()
Gbsus4 = GbM.sus4()
Gb7sus4 = Gbdom7.sus4()
# Gb minor
Gbm7 = Gbm.seventh()
GbmM7 = Gbm.major_seventh()
Gbm6 = Gbm.sixth()
Gbmb5 = Gbm.b5()
Gbm7b5 = Gbm.seventh_b5()
# Gb augmented
Gbaug7 = Gbaug.seventh()
GbaugM7 = Gbaug.major_seventh()
# Gb diminished
Gbdim7 = Gbdim.seventh()
Gbhalfdim7 = Gbdim.half_seventh()
""" Gs Chords"""
# Gs basic
GsM = Major_Triad(sa)
Gsm = Minor_Triad(sa)
Gsaug = Aug_Triad(sa)
Gsdim = Dim_Triad(sa)
# Gs Major
GsM7 = GsM.major_seventh()
GsM6 = GsM.sixth()
Gsdom7 = GsM.dominant_seventh()
Gsdom9 = GsM.dominant_ninth()
Gsdom11 = GsM.dominant_eleventh()
Gsdom13 = GsM.dominant_thirteenth()
Gsadd9 = GsM.add(['M9'])
Gs7add9 = Gsdom7.add(['M9'])
GsM7add9 = GsM7.add(['M9'])
Gsadd11 = GsM.add(['P11'])
Gs69 = GsM.add(['M6','M9'])
Gssus2 = GsM.sus2()
Gssus4 = GsM.sus4()
Gs7sus4 = Gsdom7.sus4()
# Gs minor
Gsm7 = Gsm.seventh()
GsmM7 = Gsm.major_seventh()
Gsm6 = Gsm.sixth()
Gsmb5 = Gsm.b5()
Gsm7b5 = Gsm.seventh_b5()
# Gs augmented
Gsaug7 = Gsaug.seventh()
GsaugM7 = Gsaug.major_seventh()
# Gs diminished
Gsdim7 = Gsdim.seventh()
Gshalfdim7 = Gsdim.half_seventh()
""" Ab Chords"""
# Ab basic
AbM = Major_Triad(sa)
Abm = Minor_Triad(sa)
Abaug = Aug_Triad(sa)
Abdim = Dim_Triad(sa)
# Ab Major
AbM7 = AbM.major_seventh()
AbM6 = AbM.sixth()
Abdom7 = AbM.dominant_seventh()
Abdom9 = AbM.dominant_ninth()
Abdom11 = AbM.dominant_eleventh()
Abdom13 = AbM.dominant_thirteenth()
Abadd9 = AbM.add(['M9'])
Ab7add9 = Abdom7.add(['M9'])
AbM7add9 = AbM7.add(['M9'])
Abadd11 = AbM.add(['P11'])
Ab69 = AbM.add(['M6','M9'])
Absus2 = AbM.sus2()
Absus4 = AbM.sus4()
Ab7sus4 = Abdom7.sus4()
# Ab minor
Abm7 = Abm.seventh()
AbmM7 = Abm.major_seventh()
Abm6 = Abm.sixth()
Abmb5 = Abm.b5()
Abm7b5 = Abm.seventh_b5()
# Ab augmented
Abaug7 = Abaug.seventh()
AbaugM7 = Abaug.major_seventh()
# Ab diminished
Abdim7 = Abdim.seventh()
Abhalfdim7 = Abdim.half_seventh()
""" As Chords"""
# As basic
AsM = Major_Triad(chi)
Asm = Minor_Triad(chi)
Asaug = Aug_Triad(chi)
Asdim = Dim_Triad(chi)
# As Major
AsM7 = AsM.major_seventh()
AsM6 = AsM.sixth()
Asdom7 = AsM.dominant_seventh()
Asdom9 = AsM.dominant_ninth()
Asdom11 = AsM.dominant_eleventh()
Asdom13 = AsM.dominant_thirteenth()
Asadd9 = AsM.add(['M9'])
As7add9 = Asdom7.add(['M9'])
AsM7add9 = AsM7.add(['M9'])
Asadd11 = AsM.add(['P11'])
As69 = AsM.add(['M6','M9'])
Assus2 = AsM.sus2()
Assus4 = AsM.sus4()
As7sus4 = Asdom7.sus4()
# As minor
Asm7 = Asm.seventh()
AsmM7 = Asm.major_seventh()
Asm6 = Asm.sixth()
Asmb5 = Asm.b5()
Asm7b5 = Asm.seventh_b5()
# As augmented
Asaug7 = Asaug.seventh()
AsaugM7 = Asaug.major_seventh()
# As diminished
Asdim7 = Asdim.seventh()
Ashalfdim7 = Asdim.half_seventh()
""" Bb Chords"""
# Bb basic
BbM = Major_Triad(chi)
Bbm = Minor_Triad(chi)
Bbaug = Aug_Triad(chi)
Bbdim = Dim_Triad(chi)
# Bb Major
BbM7 = BbM.major_seventh()
BbM6 = BbM.sixth()
Bbdom7 = BbM.dominant_seventh()
Bbdom9 = BbM.dominant_ninth()
Bbdom11 = BbM.dominant_eleventh()
Bbdom13 = BbM.dominant_thirteenth()
Bbadd9 = BbM.add(['M9'])
Bb7add9 = Bbdom7.add(['M9'])
BbM7add9 = BbM7.add(['M9'])
Bbadd11 = BbM.add(['P11'])
Bb69 = BbM.add(['M6','M9'])
Bbsus2 = BbM.sus2()
Bbsus4 = BbM.sus4()
Bb7sus4 = Bbdom7.sus4()
# Bb minor
Bbm7 = Bbm.seventh()
BbmM7 = Bbm.major_seventh()
Bbm6 = Bbm.sixth()
Bbmb5 = Bbm.b5()
Bbm7b5 = Bbm.seventh_b5()
# Bb augmented
Bbaug7 = Bbaug.seventh()
BbaugM7 = Bbaug.major_seventh()
# Bb diminished
Bbdim7 = Bbdim.seventh()
Bbhalfdim7 = Bbdim.half_seventh()
""" Bs Chords"""
# Bs basic
BsM = Major_Triad(do)
Bsm = Minor_Triad(do)
Bsaug = Aug_Triad(do)
Bsdim = Dim_Triad(do)
# Bs Major
BsM7 = BsM.major_seventh()
BsM6 = BsM.sixth()
Bsdom7 = BsM.dominant_seventh()
Bsdom9 = BsM.dominant_ninth()
Bsdom11 = BsM.dominant_eleventh()
Bsdom13 = BsM.dominant_thirteenth()
Bsadd9 = BsM.add(['M9'])
Bs7add9 = Bsdom7.add(['M9'])
BsM7add9 = BsM7.add(['M9'])
Bsadd11 = BsM.add(['P11'])
Bs69 = BsM.add(['M6','M9'])
Bssus2 = BsM.sus2()
Bssus4 = BsM.sus4()
Bs7sus4 = Bsdom7.sus4()
# Bs minor
Bsm7 = Bsm.seventh()
BsmM7 = Bsm.major_seventh()
Bsm6 = Bsm.sixth()
Bsmb5 = Bsm.b5()
Bsm7b5 = Bsm.seventh_b5()
# Bs augmented
Bsaug7 = Bsaug.seventh()
BsaugM7 = Bsaug.major_seventh()
# Bs diminished
Bsdim7 = Bsdim.seventh()
Bshalfdim7 = Bsdim.half_seventh()

CHORD = dict({'C':CM,'Cm':Cm,'Caug':Caug,'Cdim':Cdim,'CM7':CM7,'CM6':CM6,'C7':Cdom7,'C9':Cdom9,'C11':Cdom11,'C13':Cdom13,'Cadd9':Cadd9,'C7add9':C7add9,'CM7add9':CM7add9,'Cadd11':Cadd11,'C69':C69,'Csus2':Csus2,'Csus4':Csus4,'C7sus4':C7sus4,'Cm7':Cm7,'CmM7':CmM7,'Cm6':Cm6,'Cmb5':Cmb5,'Cm7b5':Cm7b5,'Caug7':Caug7,'CaugM7':CaugM7,'Cdim7':Cdim7,'Chalfdim7':Chalfdim7
,'D':DM,'Dm':Dm,'Daug':Daug,'Ddim':Ddim,'DM7':DM7,'DM6':DM6,'D7':Ddom7,'D9':Ddom9,'D11':Ddom11,'D13':Ddom13,'Dadd9':Dadd9,'D7add9':D7add9,'DM7add9':DM7add9,'Dadd11 ':Dadd11 ,'D69':D69,'Dsus2':Dsus2,'Dsus4':Dsus4,'D7sus4':D7sus4,'Dm7':Dm7,'DmM7':DmM7,'Dm6 ':Dm6 ,'Dmb5':Dmb5,'Dm7b5':Dm7b5,'Daug7':Daug7,'DaugM7':DaugM7,'Ddim7':Ddim7,'Dhalfdim7':Dhalfdim7
,'E':EM,'Em':Em,'Eaug':Eaug,'Edim':Edim,'EM7':EM7,'EM6':EM6,'E7':Edom7,'E9':Edom9,'E11':Edom11,'E13':Edom13,'Eadd9':Eadd9,'E7add9':E7add9,'EM7add9':EM7add9,'Eadd11 ':Eadd11 ,'E69':E69,'Esus2':Esus2,'Esus4':Esus4,'E7sus4':E7sus4,'Em7':Em7,'EmM7':EmM7,'Em6 ':Em6 ,'Emb5':Emb5,'Em7b5':Em7b5,'Eaug7':Eaug7,'EaugM7':EaugM7,'Edim7':Edim7,'Ehalfdim7':Ehalfdim7
,'F':FM,'Fm':Fm,'Faug':Faug,'Fdim':Fdim,'FM7':FM7,'FM6':FM6,'F7':Fdom7,'F9':Fdom9,'F11':Fdom11,'F13':Fdom13,'Fadd9':Fadd9,'F7add9':F7add9,'FM7add9':FM7add9,'Fadd11 ':Fadd11 ,'F69':F69,'Fsus2':Fsus2,'Fsus4':Fsus4,'F7sus4':F7sus4,'Fm7':Fm7,'FmM7':FmM7,'Fm6 ':Fm6 ,'Fmb5':Fmb5,'Fm7b5':Fm7b5,'Faug7':Faug7,'FaugM7':FaugM7,'Fdim7':Fdim7,'Fhalfdim7':Fhalfdim7
,'G':GM,'Gm':Gm,'Gaug':Gaug,'Gdim':Gdim,'GM7':GM7,'GM6':GM6,'G7':Gdom7,'G9':Gdom9,'G11':Adom11,'G13':Adom13,'Gadd9':Gadd9,'G7add9':G7add9,'GM7add9':GM7add9,'Gadd11 ':Gadd11 ,'G69':G69,'Gsus2':Gsus2,'Gsus4':Gsus4,'G7sus4':G7sus4,'Gm7':Gm7,'GmM7':GmM7,'Gm6 ':Gm6 ,'Gmb5':Gmb5,'Gm7b5':Gm7b5,'Gaug7':Gaug7,'GaugM7':GaugM7,'Gdim7':Gdim7,'Ghalfdim7':Ghalfdim7
,'A':AM,'Am':Am,'Aaug':Aaug,'Adim':Adim,'AM7':AM7,'AM6':AM6,'A7':Adom7,'A9':Adom9,'A11':Gdom11,'A13':Gdom13,'Aadd9':Aadd9,'A7add9':A7add9,'AM7add9':AM7add9,'Aadd11 ':Aadd11 ,'A69':A69,'Asus2':Asus2,'Asus4':Asus4,'A7sus4':A7sus4,'Am7':Am7,'AmM7':AmM7,'Am6 ':Am6 ,'Amb5':Amb5,'Am7b5':Am7b5,'Aaug7':Aaug7,'AaugM7':AaugM7,'Adim7':Adim7,'Ahalfdim7':Ahalfdim7
,'B':BM,'Bm':Bm,'Baug':Baug,'Bdim':Bdim,'BM7':BM7,'BM6':BM6,'B7':Bdom7,'B9':Bdom9,'B11':Bdom11,'B13':Bdom13,'Badd9':Badd9,'B7add9':B7add9,'BM7add9':BM7add9,'Badd11 ':Badd11 ,'B69':B69,'Bsus2':Bsus2,'Bsus4':Bsus4,'B7sus4':B7sus4,'Bm7':Bm7,'BmM7':BmM7,'Bm6 ':Bm6 ,'Bmb5':Bmb5,'Bm7b5':Bm7b5,'Baug7':Baug7,'BaugM7':BaugM7,'Bdim7':Bdim7,'Bhalfdim7':Bhalfdim7
,'Cb':CbM,'Cbm':Cbm,'Cbaug':Cbaug,'Cbdim':Cbdim,'CbM7':CbM7,'CbM6':CbM6,'Cb7':Cbdom7,'Cb9':Cbdom9,'Cb11':Cbdom11,'Cb13':Cbdom13,'Cbadd9':Cbadd9,'Cb7add9':Cb7add9,'CbM7add9':CbM7add9,'Cbadd11 ':Cbadd11 ,'Cb69':Cb69,'Cbsus2':Cbsus2,'Cbsus4':Cbsus4,'Cb7sus4':Cb7sus4,'Cbm7':Cbm7,'CbmM7':CbmM7,'Cbm6 ':Cbm6 ,'Cbmb5':Cbmb5,'Cbm7b5':Cbm7b5,'Cbaug7':Cbaug7,'CbaugM7':CbaugM7,'Cbdim7':Cbdim7,'Cbhalfdim7':Cbhalfdim7
,'Cs':CsM,'Csm':Csm,'Csaug':Csaug,'Csdim':Csdim,'CsM7':CsM7,'CsM6':CsM6,'Cs7':Csdom7,'Cs9':Csdom9,'Cs11':Csdom11,'Cs13':Csdom13,'Csadd9':Csadd9,'Cs7add9':Cs7add9,'CsM7add9':CsM7add9,'Csadd11 ':Csadd11 ,'Cs69':Cs69,'Cssus2':Cssus2,'Cssus4':Cssus4,'Cs7sus4':Cs7sus4,'Csm7':Csm7,'CsmM7':CsmM7,'Csm6 ':Csm6 ,'Csmb5':Csmb5,'Csm7b5':Csm7b5,'Csaug7':Csaug7,'CsaugM7':CsaugM7,'Csdim7':Csdim7,'Cshalfdim7':Cshalfdim7
,'Db':DbM,'Dbm':Dbm,'Dbaug':Dbaug,'Dbdim':Dbdim,'DbM7':DbM7,'DbM6':DbM6,'Db7':Dbdom7,'Db9':Dbdom9,'Db11':Dbdom11,'Db13':Dbdom13,'Dbadd9':Dbadd9,'Db7add9':Db7add9,'DbM7add9':DbM7add9,'Dbadd11 ':Dbadd11 ,'Db69':Db69,'Dbsus2':Dbsus2,'Dbsus4':Dbsus4,'Db7sus4':Db7sus4,'Dbm7':Dbm7,'DbmM7':DbmM7,'Dbm6 ':Dbm6 ,'Dbmb5':Dbmb5,'Dbm7b5':Dbm7b5,'Dbaug7':Dbaug7,'DbaugM7':DbaugM7,'Dbdim7':Dbdim7,'Dbhalfdim7':Dbhalfdim7
,'Ds':DsM,'Dsm':Dsm,'Dsaug':Dsaug,'Dsdim':Dsdim,'DsM7':DsM7,'DsM6':DsM6,'Ds7':Dsdom7,'Ds9':Dsdom9,'Ds11':Dsdom11,'Ds13':Dsdom13,'Dsadd9':Dsadd9,'Ds7add9':Ds7add9,'DsM7add9':DsM7add9,'Dsadd11 ':Dsadd11 ,'Ds69':Ds69,'Dssus2':Dssus2,'Dssus4':Dssus4,'Ds7sus4':Ds7sus4,'Dsm7':Dsm7,'DsmM7':DsmM7,'Dsm6 ':Dsm6 ,'Dsmb5':Dsmb5,'Dsm7b5':Dsm7b5,'Dsaug7':Dsaug7,'DsaugM7':DsaugM7,'Dsdim7':Dsdim7,'Dshalfdim7':Dshalfdim7
,'Eb':EbM,'Ebm':Ebm,'Ebaug':Ebaug,'Ebdim':Ebdim,'EbM7':EbM7,'EbM6':EbM6,'Eb7':Ebdom7,'Eb9':Ebdom9,'Eb11':Ebdom11,'Eb13':Ebdom13,'Ebadd9':Ebadd9,'Eb7add9':Eb7add9,'EbM7add9':EbM7add9,'Ebadd11 ':Ebadd11 ,'Eb69':Eb69,'Ebsus2':Ebsus2,'Ebsus4':Ebsus4,'Eb7sus4':Eb7sus4,'Ebm7':Ebm7,'EbmM7':EbmM7,'Ebm6 ':Ebm6 ,'Ebmb5':Ebmb5,'Ebm7b5':Ebm7b5,'Ebaug7':Ebaug7,'EbaugM7':EbaugM7,'Ebdim7':Ebdim7,'Ebhalfdim7':Ebhalfdim7
,'Es':EsM,'Esm':Esm,'Esaug':Esaug,'Esdim':Esdim,'EsM7':EsM7,'EsM6':EsM6,'Es7':Esdom7,'Es9':Esdom9,'Es11':Esdom11,'Es13':Esdom13,'Esadd9':Esadd9,'Es7add9':Es7add9,'EsM7add9':EsM7add9,'Esadd11 ':Esadd11 ,'Es69':Es69,'Essus2':Essus2,'Essus4':Essus4,'Es7sus4':Es7sus4,'Esm7':Esm7,'EsmM7':EsmM7,'Esm6 ':Esm6 ,'Esmb5':Esmb5,'Esm7b5':Esm7b5,'Esaug7':Esaug7,'EsaugM7':EsaugM7,'Esdim7':Esdim7,'Eshalfdim7':Eshalfdim7
,'Fs':FsM,'Fsm':Fsm,'Fsaug':Fsaug,'Fsdim':Fsdim,'FsM7':FsM7,'FsM6':FsM6,'Fs7':Fsdom7,'Fs9':Fsdom9,'Fs11':Fsdom11,'Fs13':Fsdom13,'Fsadd9':Fsadd9,'Fs7add9':Fs7add9,'FsM7add9':FsM7add9,'Fsadd11 ':Fsadd11 ,'Fs69':Fs69,'Fssus2':Fssus2,'Fssus4':Fssus4,'Fs7sus4':Fs7sus4,'Fsm7':Fsm7,'FsmM7':FsmM7,'Fsm6 ':Fsm6 ,'Fsmb5':Fsmb5,'Fsm7b5':Fsm7b5,'Fsaug7':Fsaug7,'FsaugM7':FsaugM7,'Fsdim7':Fsdim7,'Fshalfdim7':Fshalfdim7
,'Gb':GbM,'Gbm':Gbm,'Gbaug':Gbaug,'Gbdim':Gbdim,'GbM7':GbM7,'GbM6':GbM6,'Gb7':Gbdom7,'Gb9':Gbdom9,'Gb11':Gbdom11,'Gb13':Gbdom13,'Gbadd9':Gbadd9,'Gb7add9':Gb7add9,'GbM7add9':GbM7add9,'Gbadd11 ':Gbadd11 ,'Gb69':Gb69,'Gbsus2':Gbsus2,'Gbsus4':Gbsus4,'Gb7sus4':Gb7sus4,'Gbm7':Gbm7,'GbmM7':GbmM7,'Gbm6 ':Gbm6 ,'Gbmb5':Gbmb5,'Gbm7b5':Gbm7b5,'Gbaug7':Gbaug7,'GbaugM7':GbaugM7,'Gbdim7':Gbdim7,'Gbhalfdim7':Gbhalfdim7
,'Gs':GsM,'Gsm':Gsm,'Gsaug':Gsaug,'Gsdim':Gsdim,'GsM7':GsM7,'GsM6':GsM6,'Gs7':Gsdom7,'Gs9':Gsdom9,'Gs11':Gsdom11,'Gs13':Gsdom13,'Gsadd9':Gsadd9,'Gs7add9':Gs7add9,'GsM7add9':GsM7add9,'Gsadd11 ':Gsadd11 ,'Gs69':Gs69,'Gssus2':Gssus2,'Gssus4':Gssus4,'Gs7sus4':Gs7sus4,'Gsm7':Gsm7,'GsmM7':GsmM7,'Gsm6 ':Gsm6 ,'Gsmb5':Gsmb5,'Gsm7b5':Gsm7b5,'Gsaug7':Gsaug7,'GsaugM7':GsaugM7,'Gsdim7':Gsdim7,'Gshalfdim7':Gshalfdim7
,'Ab':AbM,'Abm':Abm,'Abaug':Abaug,'Abdim':Abdim,'AbM7':AbM7,'AbM6':AbM6,'Ab7':Abdom7,'Ab9':Abdom9,'Ab11':Abdom11,'Ab13':Abdom13,'Abadd9':Abadd9,'Ab7add9':Ab7add9,'AbM7add9':AbM7add9,'Abadd11 ':Abadd11 ,'Ab69':Ab69,'Absus2':Absus2,'Absus4':Absus4,'Ab7sus4':Ab7sus4,'Abm7':Abm7,'AbmM7':AbmM7,'Abm6 ':Abm6 ,'Abmb5':Abmb5,'Abm7b5':Abm7b5,'Abaug7':Abaug7,'AbaugM7':AbaugM7,'Abdim7':Abdim7,'Abhalfdim7':Abhalfdim7
,'As':AsM,'Asm':Asm,'Asaug':Asaug,'Asdim':Asdim,'AsM7':AsM7,'AsM6':AsM6,'As7':Asdom7,'As9':Asdom9,'As11':Asdom11,'As13':Asdom13,'Asadd9':Asadd9,'As7add9':As7add9,'AsM7add9':AsM7add9,'Asadd11 ':Asadd11 ,'As69':As69,'Assus2':Assus2,'Assus4':Assus4,'As7sus4':As7sus4,'Asm7':Asm7,'AsmM7':AsmM7,'Asm6 ':Asm6 ,'Asmb5':Asmb5,'Asm7b5':Asm7b5,'Asaug7':Asaug7,'AsaugM7':AsaugM7,'Asdim7':Asdim7,'Ashalfdim7':Ashalfdim7
,'Bb':BbM,'Bbm':Bbm,'Bbaug':Bbaug,'Bbdim':Bbdim,'BbM7':BbM7,'BbM6':BbM6,'Bb7':Bbdom7,'Bb9':Bbdom9,'Bb11':Bbdom11,'Bb13':Bbdom13,'Bbadd9':Bbadd9,'Bb7add9':Bb7add9,'BbM7add9':BbM7add9,'Bbadd11 ':Bbadd11 ,'Bb69':Bb69,'Bbsus2':Bbsus2,'Bbsus4':Bbsus4,'Bb7sus4':Bb7sus4,'Bbm7':Bbm7,'BbmM7':BbmM7,'Bbm6 ':Bbm6 ,'Bbmb5':Bbmb5,'Bbm7b5':Bbm7b5,'Bbaug7':Bbaug7,'BbaugM7':BbaugM7,'Bbdim7':Bbdim7,'Bbhalfdim7':Bbhalfdim7
,'Bs':BsM,'Bsm':Bsm,'Bsaug':Bsaug,'Bsdim':Bsdim,'BsM7':BsM7,'BsM6':BsM6,'Bs7':Bsdom7,'Bs9':Bsdom9,'Bs11':Bsdom11,'Bs13':Bsdom13,'Bsadd9':Bsadd9,'Bs7add9':Bs7add9,'BsM7add9':BsM7add9,'Bsadd11 ':Bsadd11 ,'Bs69':Bs69,'Bssus2':Bssus2,'Bssus4':Bssus4,'Bs7sus4':Bs7sus4,'Bsm7':Bsm7,'BsmM7':BsmM7,'Bsm6 ':Bsm6 ,'Bsmb5':Bsmb5,'Bsm7b5':Bsm7b5,'Bsaug7':Bsaug7,'BsaugM7':BsaugM7,'Bsdim7':Bsdim7,'Bshalfdim7':Bshalfdim7})