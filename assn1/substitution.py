import collections

def solve_substitution(ciphertext):
    """
    Decrypts using a mapped dictionary derived from frequency analysis
    and known words like 'Multi-factor authentication'.
    """
    # Mapping derived from the crib "Multi-factor authentication" and "Third-party"
    # Cipher char -> Plain char
    key_map = {
        '%': ' ', ':': 't', 'B': 'h', 'V': 'e', ')': 'o',
        'u': 'a', 'G':'n', 'o':'i', '9':'c','u':'a','s':'u',
        '"': 's', 'F': 'r', '3':'m','@':'l','U':'-','M':'f',
        'T':'b','X':'w',']':'y','8':'g',"'":'d','Q':'k',
        '~':'p','*':'v','J':'I','!':'.', '|':'q','H':'M','R':'S',
        'b':'G','?':'F','6':'z','v':',','C':'j','&':'D','\\':'P',
        'N':'A','>':'W','f':'2','#':'0','r':'8','d':'R','l':'T','{':'E',
        '(':'x','.':'K','+':'U','a':'[','w':'6','_':'C','P':'1','e':'3',
        '<':'4','j':'L', 'x':'(','A':',','}':'5','m':'9','i':'7','`':')',
        '/':'H','D':'O','W':']','L':'&',';':'B','4':"'",'p':'V','k':'N',
        'q':'"', " ": ':', 'k':'N','0':'j'
    }

    plaintext = []
    for char in ciphertext:
        if char in key_map:
            plaintext.append(key_map[char])
        elif char == '\n':
            plaintext.append('\n')
        else:
            # Keep unknown characters as is to spot them
            plaintext.append(f"[{char}]") 

    text = "".join(plaintext)            

    print(text)



ciphertext = r"""
Hs@:oUMu9:)F%us:BVG:o9u:o)G%xH?NA%VG9)3~u""oG8%lX)UMu9:)F%us:BVG:o9u:o)G%)F%f?Nv%u@)G8%Xo:B%"o3o@uF%:VF3"`%o"%uG%V@V9:F)Go9%us:BVG:o9u:o)G%3V:B)'%oG%XBo9B%u%9)3~s:VF%s"VF%o"%8FuG:V'%u99V""%:)%u%XVT"o:V%)F%u~~@o9u:o)G%)G@]%uM:VF%"s99V""Ms@@]%~FV"VG:oG8%:X)%)F%3)FV%~oV9V"%)M%V*o'VG9V%x)F%Mu9:)F"`%:)%uG%us:BVG:o9u:o)G%3V9BuGo"3 %QG)X@V'8V%x")3V:BoG8%)G@]%:BV%s"VF%QG)X"`v%~)""V""o)G%x")3V:BoG8%)G@]%:BV%s"VF%Bu"`v%uG'%oGBVFVG9V%x")3V:BoG8%)G@]%:BV%s"VF%o"`!%H?N%~F):V9:"%:BV%s"VF%MF)3%uG%sGQG)XG%~VF")G%:F]oG8%:)%u99V""%:BVoF%'u:u%"s9B%u"%~VF")Gu@%J&%'V:uo@"%)F%MoGuG9ou@%u""V:"!


V8BX@"96u~0]s*3GQT)MF|':(o

N%:BoF'U~uF:]%us:BVG:o9u:)F%xl\N`%u~~%VGuT@V"%:X)UMu9:)F%us:BVG:o9u:o)Gv%s"su@@]%T]%"B)XoG8%u%FuG')3@]U8VGVFu:V'%uG'%9)G":uG:@]%FVMFV"BoG8%9)'V%:)%s"V%M)F%us:BVG:o9u:o)G!
_)G:VG:"

%%%%P%?u9:)F"
%%%%%%%%P!P%.G)X@V'8V
%%%%%%%%P!f%\)""V""o)G
%%%%%%%%P!e%JGBVFVG:
%%%%%%%%P!<%j)9u:o)G
%%%%f%l)QVG"
%%%%%%%%f!P%N'*uG9V"%oG%3)To@V%:X)UMu9:)F%us:BVG:o9u:o)G
%%%%e%jV8o"@u:o)G%uG'%FV8s@u:o)G
%%%%%%%%e!P%{sF)~VuG%+Go)G
%%%%%%%%e!f%JG'ou
%%%%%%%%e!e%+Go:V'%R:u:V"
%%%%<%RV9sFo:]
%%%%}%J3~@V3VG:u:o)G
%%%%w%\u:VG:"
%%%%i%{(u3~@V"
%%%%r%RVV%u@")
%%%%m%dVMVFVG9V"
%%%%P#%?sF:BVF%FVu'oG8
%%%%PP%{(:VFGu@%@oGQ"

?u9:)F"

Ns:BVG:o9u:o)G%:uQV"%~@u9V%XBVG%")3V)GV%:FoV"%:)%@)8%oG:)%u%9)3~s:VF%FV")sF9V%x"s9B%u"%u%GV:X)FQv%'V*o9Vv%)F%u~~@o9u:o)G`!%lBV%FV")sF9V%FV|soFV"%:BV%s"VF%:)%"s~~@]%:BV%o'VG:o:]%T]%XBo9B%:BV%s"VF%o"%QG)XG%:)%:BV%FV")sF9Vv%u@)G8%Xo:B%V*o'VG9V%)M%:BV%us:BVG:o9o:]%)M%:BV%s"VF4"%9@uo3%:)%:Bu:%o'VG:o:]!%Ro3~@V%us:BVG:o9u:o)G%FV|soFV"%)G@]%)GV%"s9B%~oV9V%)M%V*o'VG9V%xMu9:)F`v%:]~o9u@@]%u%~u""X)F'!%?)F%u''o:o)Gu@%"V9sFo:]v%:BV%FV")sF9V%3u]%FV|soFV%3)FV%:BuG%)GV%Mu9:)F3s@:oUMu9:)F%us:BVG:o9u:o)Gv%)F%:X)UMu9:)F%us:BVG:o9u:o)G%oG%9u"V"%XBVFV%V(u9:@]%:X)%~oV9V"%)M%V*o'VG9V%uFV%:)%TV%"s~~@oV'!aPW

lBV%s"V%)M%3s@:o~@V%us:BVG:o9u:o)G%Mu9:)F"%:)%~F)*V%)GV4"%o'VG:o:]%o"%Tu"V'%)G%:BV%~FV3o"V%:Bu:%uG%sGus:B)Fo6V'%u9:)F%o"%sG@oQV@]%:)%TV%uT@V%:)%"s~~@]%:BV%Mu9:)F"%FV|soFV'%M)F%u99V""!%JMv%oG%uG%us:BVG:o9u:o)G%u::V3~:v%u:%@Vu":%)GV%)M%:BV%9)3~)GVG:"%o"%3o""oG8%)F%"s~~@oV'%oG9)FFV9:@]v%:BV%s"VF4"%o'VG:o:]%o"%G):%V":uT@o"BV'%Xo:B%"sMMo9oVG:%9VF:uoG:]%uG'%u99V""%:)%:BV%u""V:%xV!8!v%u%Tso@'oG8v%)F%'u:u`%TVoG8%~F):V9:V'%T]%3s@:oUMu9:)F%us:BVG:o9u:o)G%:BVG%FV3uoG"%T@)9QV'!%lBV%us:BVG:o9u:o)G%Mu9:)F"%)M%u%3s@:oUMu9:)F%us:BVG:o9u:o)G%"9BV3V%3u]%oG9@s'V afW

%%%%R)3V:BoG8%:BV%s"VF%Bu" %R)3V%~B]"o9u@%)T0V9:%oG%:BV%~)""V""o)G%)M%:BV%s"VFv%"s9B%u"%u%"V9sFo:]%:)QVG%x+R;%":o9Q`v%u%TuGQ%9uF'v%u%QV]v%V:9!
%%%%R)3V:BoG8%:BV%s"VF%QG)X" %_VF:uoG%QG)X@V'8V%)G@]%QG)XG%:)%:BV%s"VFv%"s9B%u"%u%~u""X)F'v%\Jkv%lNkv%V:9!
%%%%R)3V:BoG8%:BV%s"VF%o" %R)3V%~B]"o9u@%9BuFu9:VFo":o9%)M%:BV%s"VF%xTo)3V:Fo9"`v%"s9B%u"%u%MoG8VF~FoG:v%V]V%oFo"v%*)o9Vv%:]~oG8%"~VV'v%~u::VFG%oG%QV]%~FV""%oG:VF*u@"v%V:9!
%%%%R)3VXBVFV%:BV%s"VF%o" %R)3V%9)GGV9:o)G%:)%u%"~V9oMo9%9)3~s:oG8%GV:X)FQ%)F%s"oG8%u%b\R%"o8Gu@%:)%o'VG:oM]%:BV%@)9u:o)G!aeW

N%8))'%V(u3~@V%)M%:X)UMu9:)F%us:BVG:o9u:o)G%o"%:BV%Xo:B'FuXoG8%)M%3)GV]%MF)3%uG%NlHA%)G@]%:BV%9)FFV9:%9)3ToGu:o)G%)M%u%TuGQ%9uF'%x")3V:BoG8%:BV%s"VF%~)""V""V"`%uG'%u%\Jk%x")3V:BoG8%:BV%s"VF%QG)X"`%u@@)X"%:BV%:FuG"u9:o)G%:)%TV%9uFFoV'%)s:!%lX)%):BVF%V(u3~@V"%uFV%:)%"s~~@V3VG:%u%s"VFU9)G:F)@@V'%~u""X)F'%Xo:B%u%)GVU:o3V%~u""X)F'%xDl\`%)F%9)'V%8VGVFu:V'%)F%FV9Vo*V'%T]%uG%us:BVG:o9u:)F%xV!8!%u%"V9sFo:]%:)QVG%)F%"3uF:~B)GV`%:Bu:%)G@]%:BV%s"VF%~)""V""V"!a9o:u:o)G%GVV'V'W

N%:BoF'U~uF:]%us:BVG:o9u:)F%u~~%VGuT@V"%:X)UMu9:)F%us:BVG:o9u:o)G%oG%u%'oMMVFVG:%Xu]v%s"su@@]%T]%"B)XoG8%u%FuG')3@]U8VGVFu:V'%uG'%9)G":uG:@]%FVMFV"BoG8%9)'V%XBo9B%:BV%s"VF%9uG%s"Vv%Fu:BVF%:BuG%"VG'oG8%uG%RHR%)F%s"oG8%uG):BVF%3V:B)'!%N%To8%TVGVMo:%)M%:BV"V%u~~"%o"%:Bu:%:BV]%s"su@@]%9)G:oGsV%:)%X)FQ%V*VG%Xo:B)s:%uG%oG:VFGV:%9)GGV9:o)G!%{(u3~@V"%)M%:BoF'U~uF:]%us:BVG:o9u:)F%u~~"%oG9@s'V%b))8@V%Ns:BVG:o9u:)Fv%Ns:B]%uG'%Ho9F)")M:%Ns:BVG:o9u:)FA%")3V%~u""X)F'%3uGu8VF"%"s9B%u"%ju":\u""%)MMVF%:BV%"VF*o9V%u"%XV@@!a<W

NG%V(u3~@V%)M%u%"V9)G'%":V~%oG%:X)U":V~%*VFoMo9u:o)G%)F%us:BVG:o9u:o)G%o"%:BV%s"VF%FV~Vu:oG8%Tu9Q%")3V:BoG8%:Bu:%Xu"%"VG:%:)%:BV3%:BF)s8B%uG%)s:U)MUTuG'%3V9BuGo"3%x"s9B%u"%u%9)'V%"VG:%)*VF%RHR`v%)F%u%Gs3TVF%8VGVFu:V'%T]%uG%u~~%:Bu:%o"%9)33)G%:)%:BV%s"VF%uG'%:BV%us:BVG:o9u:o)G%"]":V3!a}W
.G)X@V'8V

.G)X@V'8V%Mu9:)F"%uFV%:BV%3)":%9)33)G@]%s"V'%M)F3%)M%us:BVG:o9u:o)G!%JG%:Bo"%M)F3v%:BV%s"VF%o"%FV|soFV'%:)%~F)*V%QG)X@V'8V%)M%u%"V9FV:%oG%)F'VF%:)%us:BVG:o9u:V!

N%~u""X)F'%o"%u%"V9FV:%X)F'%)F%":FoG8%)M%9BuFu9:VF"%:Bu:%o"%s"V'%M)F%s"VF%us:BVG:o9u:o)G!%lBo"%o"%:BV%3)":%9)33)G@]%s"V'%3V9BuGo"3%)M%us:BVG:o9u:o)G!afW%HuG]%3s@:oUMu9:)F%us:BVG:o9u:o)G%:V9BGo|sV"%FV@]%)G%~u""X)F'%u"%)GV%Mu9:)F%)M%us:BVG:o9u:o)G!%puFou:o)G"%oG9@s'V%T):B%@)G8VF%)GV"%M)F3V'%MF)3%3s@:o~@V%X)F'"%xu%~u""~BFu"V`%uG'%:BV%"B)F:VFv%~sFV@]%Gs3VFo9v%~VF")Gu@%o'VG:oMo9u:o)G%Gs3TVF%x\Jk`%9)33)G@]%s"V'%M)F%NlH%u99V""!%lFu'o:o)Gu@@]v%~u""X)F'"%uFV%V(~V9:V'%:)%TV%3V3)Fo6V'!

HuG]%"V9FV:%|sV":o)G"%"s9B%u"%q>BVFV%XVFV%])s%T)FGgq%uFV%~))F%V(u3~@V"%)M%u%QG)X@V'8V%Mu9:)F%TV9us"V%:BV]%3u]%TV%QG)XG%:)%u%Xo'V%8F)s~%)M%~V)~@Vv%)F%TV%uT@V%:)%TV%FV"VuF9BV'!
\)""V""o)G
dRN%RV9sFJ&%:)QVGv%uG%V(u3~@V%)M%u%'o"9)GGV9:V'%:)QVG%8VGVFu:)F

\)""V""o)G%Mu9:)F"%xq")3V:BoG8%)G@]%:BV%s"VF%Bu"q`%Bu*V%TVVG%s"V'%M)F%us:BVG:o9u:o)G%M)F%9VG:sFoV"v%oG%:BV%M)F3%)M%u%QV]%:)%u%@)9Q!%lBV%Tu"o9%~FoG9o~@V%o"%:Bu:%:BV%QV]%V3T)'oV"%u%"V9FV:%XBo9B%o"%"BuFV'%TV:XVVG%:BV%@)9Q%uG'%:BV%QV]v%uG'%:BV%"u3V%~FoG9o~@V%sG'VF@oV"%~)""V""o)G%Mu9:)F%us:BVG:o9u:o)G%oG%9)3~s:VF%"]":V3"!%N%"V9sFo:]%:)QVG%o"%uG%V(u3~@V%)M%u%~)""V""o)G%Mu9:)F!

&o"9)GGV9:V'%:)QVG"%Bu*V%G)%9)GGV9:o)G"%:)%:BV%9@oVG:%9)3~s:VF!%lBV]%:]~o9u@@]%s"V%u%Tso@:UoG%"9FVVG%:)%'o"~@u]%:BV%8VGVFu:V'%us:BVG:o9u:o)G%'u:uv%XBo9B%o"%3uGsu@@]%:]~V'%oG%T]%:BV%s"VF!%lBo"%:]~V%)M%:)QVG%3)":@]%s"V%u%q)GVU:o3V%~u""X)F'q%:Bu:%9uG%)G@]%TV%s"V'%M)F%:Bu:%"~V9oMo9%"V""o)G!awW

_)GGV9:V'%:)QVG"%uFV%'V*o9V"%:Bu:%uFV%~B]"o9u@@]%9)GGV9:V'%:)%:BV%9)3~s:VF%:)%TV%s"V'!%lB)"V%'V*o9V"%:FuG"3o:%'u:u%us:)3u:o9u@@]!aiW%lBVFV%uFV%u%Gs3TVF%)M%'oMMVFVG:%:]~V"v%oG9@s'oG8%9uF'%FVu'VF"v%XoFV@V""%:u8"%uG'%+R;%:)QVG"!aiW

N%")M:XuFV%:)QVG%xu!Q!u!%")M:%:)QVG`%o"%u%:]~V%)M%:X)UMu9:)F%us:BVG:o9u:o)G%"V9sFo:]%'V*o9V%:Bu:%3u]%TV%s"V'%:)%us:B)Fo6V%:BV%s"V%)M%9)3~s:VF%"VF*o9V"!%R)M:XuFV%:)QVG"%uFV%":)FV'%)G%u%8VGVFu@U~sF~)"V%V@V9:F)Go9%'V*o9V%"s9B%u"%u%'V"Q:)~%9)3~s:VFv%@u~:)~v%\&Nv%)F%3)To@V%~B)GV%uG'%9uG%TV%'s~@o9u:V'!%x_)G:Fu":%BuF'XuFV%:)QVG"v%XBVFV%:BV%9FV'VG:ou@"%uFV%":)FV'%)G%u%'V'o9u:V'%BuF'XuFV%'V*o9V%uG'%:BVFVM)FV%9uGG):%TV%'s~@o9u:V'v%uT"VG:%~B]"o9u@%oG*u"o)G%)M%:BV%'V*o9V!`%N%")M:%:)QVG%3u]%G):%TV%u%'V*o9V%:BV%s"VF%oG:VFu9:"%Xo:B!%l]~o9u@@]%uG%^!}#m*e%9VF:oMo9u:V%o"%@)u'V'%)G:)%:BV%'V*o9V%uG'%":)FV'%"V9sFV@]%:)%"VF*V%:Bo"%~sF~)"V!
JGBVFVG:

lBV"V%uFV%Mu9:)F"%u"")9ou:V'%Xo:B%:BV%s"VFv%uG'%uFV%s"su@@]%To)3V:Fo9%3V:B)'"v%oG9@s'oG8%MoG8VF~FoG:v%Mu9Vv%*)o9Vv%)F%oFo"%FV9)8Go:o)G!%;VBu*o)Fu@%To)3V:Fo9"%"s9B%u"%QV]":F)QV%']Gu3o9"%9uG%u@")%TV%s"V'!
j)9u:o)G
HuoG%uF:o9@V %j)9u:o)GUTu"V'%us:BVG:o9u:o)G

JG9FVu"oG8@]v%u%M)sF:B%Mu9:)F%o"%9)3oG8%oG:)%~@u]%oG*)@*oG8%:BV%~B]"o9u@%@)9u:o)G%)M%:BV%s"VF!%>Bo@V%BuF'%XoFV'%:)%:BV%9)F~)Fu:V%GV:X)FQv%u%s"VF%9)s@'%TV%u@@)XV'%:)%@)8oG%s"oG8%)G@]%u%~oG%9)'V%XBo@V%)MM%:BV%GV:X)FQ%VG:VFoG8%u%9)'V%MF)3%u%")M:%:)QVG%u"%XV@@%9)s@'%TV%FV|soFV'!%lBo"%9)s@'%TV%"VVG%u"%uG%u99V~:uT@V%":uG'uF'%XBVFV%u99V""%oG:)%:BV%)MMo9V%o"%9)G:F)@@V'!

R]":V3"%M)F%GV:X)FQ%u'3o""o)G%9)G:F)@%X)FQ%oG%"o3o@uF%Xu]"%XBVFV%])sF%@V*V@%)M%GV:X)FQ%u99V""%9uG%TV%9)G:oG8VG:%)G%:BV%"~V9oMo9%GV:X)FQ%])sF%'V*o9V%o"%9)GGV9:V'%:)v%"s9B%u"%XoMo%*"%XoFV'%9)GGV9:o*o:]!%lBo"%u@")%u@@)X"%u%s"VF%:)%3)*V%TV:XVVG%)MMo9V"%uG'%']Gu3o9u@@]%FV9Vo*V%:BV%"u3V%@V*V@%)M%GV:X)FQ%u99V""%oG%Vu9B!
l)QVG"

HuG]%3s@:oUMu9:)F%us:BVG:o9u:o)G%*VG')F"%)MMVF%3)To@V%~B)GVUTu"V'%us:BVG:o9u:o)G!%R)3V%3V:B)'"%oG9@s'V%~s"BUTu"V'%us:BVG:o9u:o)Gv%td%9)'V%Tu"V'%us:BVG:o9u:o)Gv%)GVU:o3V%~u""X)F'%us:BVG:o9u:o)G%xV*VG:UTu"V'%uG'%:o3VUTu"V'`v%uG'%RHRUTu"V'%*VFoMo9u:o)G!%RHRUTu"V'%*VFoMo9u:o)G%"sMMVF"%MF)3%")3V%"V9sFo:]%9)G9VFG"!%\B)GV"%9uG%TV%9@)GV'v%u~~"%9uG%FsG%)G%"V*VFu@%~B)GV"%uG'%9V@@U~B)GV%3uoG:VGuG9V%~VF")GGV@%9uG%FVu'%RHR%:V(:"!%k):%@Vu":v%9V@@%~B)GV"%9uG%TV%9)3~F)3o"V'%oG%8VGVFu@v%3VuGoG8%:BV%~B)GV%o"%G)%@)G8VF%")3V:BoG8%)G@]%:BV%s"VF%Bu"!

lBV%3u0)F%'FuXTu9Q%)M%us:BVG:o9u:o)G%oG9@s'oG8%")3V:BoG8%:BV%s"VF%~)""V""V"%o"%:Bu:%:BV%s"VF%3s":%9uFF]%uF)sG'%:BV%~B]"o9u@%:)QVG%x:BV%+R;%":o9Qv%:BV%TuGQ%9uF'v%:BV%QV]%)F%"o3o@uF`v%~Fu9:o9u@@]%u:%u@@%:o3V"!%j)""%uG'%:BVM:%uFV%Fo"Q"!%HuG]%)F8uGo6u:o)G"%M)FTo'%9uFF]oG8%+R;%uG'%V@V9:F)Go9%'V*o9V"%oG%)F%)s:%)M%~FV3o"V"%)XoG8%:)%3u@XuFV%uG'%'u:u%:BVM:UFo"Q"v%uG'%3)":%o3~)F:uG:%3u9BoGV"%')%G):%Bu*V%+R;%~)F:"%M)F%:BV%"u3V%FVu")G!%\B]"o9u@%:)QVG"%s"su@@]%')%G):%"9u@Vv%:]~o9u@@]%FV|soFoG8%u%GVX%:)QVG%M)F%Vu9B%GVX%u99)sG:%uG'%"]":V3!%\F)9sFoG8%uG'%"sT"V|sVG:@]%FV~@u9oG8%:)QVG"%)M%:Bo"%QoG'%oG*)@*V"%9)":"!%JG%u''o:o)Gv%:BVFV%uFV%oGBVFVG:%9)GM@o9:"%uG'%sGu*)o'uT@V%:Fu'VU)MM"%TV:XVVG%s"uTo@o:]%uG'%"V9sFo:]!arW

lX)U":V~%us:BVG:o9u:o)G%oG*)@*oG8%3)To@V%~B)GV"%uG'%"3uF:~B)GV"%~F)*o'V"%uG%u@:VFGu:o*V%:)%'V'o9u:V'%~B]"o9u@%'V*o9V"!%l)%us:BVG:o9u:Vv%~V)~@V%9uG%s"V%:BVoF%~VF")Gu@%u99V""%9)'V"%:)%:BV%'V*o9V%xo!V!%")3V:BoG8%:Bu:%)G@]%:BV%oG'o*o'su@%s"VF%QG)X"`%~@s"%u%)GVU:o3VU*u@o'v%']Gu3o9%~u""9)'Vv%:]~o9u@@]%9)G"o":oG8%)M%<%:)%w%'o8o:"!%lBV%~u""9)'V%9uG%TV%"VG:%:)%:BVoF%3)To@V%'V*o9VamW%T]%RHR%)F%9uG%TV%8VGVFu:V'%T]%u%)GVU:o3V%~u""9)'VU8VGVFu:)F%u~~!%JG%T):B%9u"V"v%:BV%u'*uG:u8V%)M%s"oG8%u%3)To@V%~B)GV%o"%:Bu:%:BVFV%o"%G)%GVV'%M)F%uG%u''o:o)Gu@%'V'o9u:V'%:)QVGv%u"%s"VF"%:VG'%:)%9uFF]%:BVoF%3)To@V%'V*o9V"%uF)sG'%u:%u@@%:o3V"!

N"%)M%f#Prv%RHR%o"%:BV%3)":%TF)u'@]Uu')~:V'%3s@:oUMu9:)F%us:BVG:o9u:o)G%3V:B)'%M)F%9)G"s3VFUMu9oG8%u99)sG:"!a9o:u:o)G%GVV'V'W%k):Xo:B":uG'oG8%:BV%~)~s@uFo:]%)M%RHR%*VFoMo9u:o)Gv%"V9sFo:]%u'*)9u:V"%Bu*V%~sT@o9@]%9Fo:o9o6V'%o:aP#W%uG'%oG%Cs@]%f#Pw%u%+Go:V'%R:u:V"%kJRl%'FuM:%8so'V@oGV%~F)~)"V'%'V~FV9u:oG8%o:%u"%u%M)F3%)M%us:BVG:o9u:o)G!aPPW%N%]VuF%@u:VF%kJRl%FVoG":u:V'%RHR%*VFoMo9u:o)G%u"%u%*u@o'%us:BVG:o9u:o)G%9BuGGV@%oG%:BV%MoGu@o6V'%8so'V@oGV!aPfW

JG%f#Pw%uG'%f#Pi%FV"~V9:o*V@]v%T):B%b))8@V%uG'%N~~@V%":uF:V'%)MMVFoG8%s"VF%:X)U":V~%us:BVG:o9u:o)G%Xo:B%~s"B%G):oMo9u:o)GafW%u"%uG%u@:VFGu:o*V%3V:B)'!aPeWaP<W

RV9sFo:]%)M%3)To@VU'V@o*VFV'%"V9sFo:]%:)QVG"%Ms@@]%'V~VG'"%)G%:BV%3)To@V%)~VFu:)F4"%)~VFu:o)Gu@%"V9sFo:]%uG'%9uG%TV%Vu"o@]%TFVu9BV'%T]%XoFV:u~~oG8%)F%RJH%9@)GoG8%T]%Gu:o)Gu@%"V9sFo:]%u8VG9oV"!aP}W

N'*uG:u8V" 

%%%%k)%u''o:o)Gu@%:)QVG"%uFV%GV9V""uF]%TV9us"V%o:%s"V"%3)To@V%'V*o9V"%:Bu:%uFV%xs"su@@]`%9uFFoV'%u@@%:BV%:o3V!
%%%%N"%:BV]%uFV%9)G":uG:@]%9BuG8V'v%']Gu3o9u@@]%8VGVFu:V'%~u""9)'V"%uFV%"uMVF%:)%s"V%:BuG%Mo(V'%x":u:o9`%@)8UoG%oGM)F3u:o)G!
%%%%&V~VG'oG8%)G%:BV%")@s:o)Gv%~u""9)'V"%:Bu:%Bu*V%TVVG%s"V'%uFV%us:)3u:o9u@@]%FV~@u9V'%oG%)F'VF%:)%VG"sFV%:Bu:%u%*u@o'%9)'V%o"%u@Xu]"%u*uo@uT@Vv%:FuG"3o""o)G2FV9V~:o)G%~F)T@V3"%')%G):%:BVFVM)FV%~FV*VG:%@)8oG"!

&o"u'*uG:u8V" 

%%%%+"VF"%3u]%":o@@%TV%"s"9V~:oT@V%:)%~Bo"BoG8%u::u9Q"!%NG%u::u9QVF%9uG%"VG'%u%:V(:%3V""u8V%:Bu:%@oGQ"%:)%u%"~))MV'%XVT"o:V%:Bu:%@))Q"%o'VG:o9u@%:)%:BV%u9:su@%XVT"o:V!%lBV%u::u9QVF%9uG%:BVG%8V:%:BV%us:BVG:o9u:o)G%9)'Vv%s"VF%Gu3V%uG'%~u""X)F'!aPwW
%%%%N%3)To@V%~B)GV%o"%G):%u@Xu]"%u*uo@uT@V:BV]%9uG%TV%@)":v%":)@VGv%Bu*V%u%'Vu'%Tu::VF]v%)F%):BVFXo"V%G):%X)FQ!
%%%%H)To@V%~B)GV%FV9V~:o)G%o"%G):%u@Xu]"%u*uo@uT@V@uF8V%uFVu"v%~uF:o9s@uF@]%)s:"o'V%)M%:)XG"v%@u9Q%9)*VFu8V!
%%%%RJH%9@)GoG8%8o*V"%Bu9QVF"%u99V""%:)%3)To@V%~B)GV%9)GGV9:o)G"!%R)9ou@UVG8oGVVFoG8%u::u9Q"%u8uoG":%3)To@VU)~VFu:)F%9)3~uGoV"%Bu*V%FV"s@:V'%oG%:BV%BuG'oG8%)*VF%)M%'s~@o9u:V%RJH%9uF'"%:)%9Fo3oGu@"!aPiW
%%%%lV(:%3V""u8V"%:)%3)To@V%~B)GV"%s"oG8%RHR%uFV%oG"V9sFV%uG'%9uG%TV%oG:VF9V~:V'%T]%JHRJU9u:9BVF"!%lBs"%:BoF'%~uF:oV"%9uG%":Vu@%uG'%s"V%:BV%:)QVG!aPrW
%%%%N99)sG:%FV9)*VF]%:]~o9u@@]%T]~u""V"%3)To@VU~B)GV%:X)UMu9:)F%us:BVG:o9u:o)G!aPmW
%%%%H)'VFG%"3uF:~B)GV"%uFV%s"V'%T):B%M)F%FV9Vo*oG8%V3uo@%uG'%RHR!%R)%oM%:BV%~B)GV%o"%@)":%)F%":)@VG%uG'%o"%G):%~F):V9:V'%T]%u%~u""X)F'%)F%To)3V:Fo9v%u@@%u99)sG:"%M)F%XBo9B%:BV%V3uo@%o"%:BV%QV]%9uG%TV%Bu9QV'%u"%:BV%~B)GV%9uG%FV9Vo*V%:BV%"V9)G'%Mu9:)F!
%%%%H)To@V%9uFFoVF"%3u]%9BuF8V%:BV%s"VF%M)F%3V""u8oG8%MVV"!

N'*uG9V"%oG%3)To@V%:X)UMu9:)F%us:BVG:o9u:o)G

N'*uG9V"%oG%FV"VuF9B%)M%:X)UMu9:)F%us:BVG:o9u:o)G%M)F%3)To@V%'V*o9V"%9)G"o'VF%'oMMVFVG:%3V:B)'"%oG%XBo9B%u%"V9)G'%Mu9:)F%9uG%TV%o3~@V3VG:V'%XBo@V%G):%~)"oG8%u%BoG'FuG9V%:)%:BV%s"VF!%>o:B%:BV%9)G:oGsV'%s"V%uG'%o3~F)*V3VG:"%oG%:BV%u99sFu9]%)M%3)To@V%BuF'XuFV%"s9B%u"%b\Rvaf#W%3o9F)~B)GVvafPW%uG'%8]F)2u99V@VF)3):VFvaffW%:BV%uTo@o:]%:)%s"V%:BV3%u"%u%"V9)G'%Mu9:)F%)M%us:BVG:o9u:o)G%o"%TV9)3oG8%3)FV%:Fs":X)F:B]!%?)F%V(u3~@Vv%T]%FV9)F'oG8%:BV%u3ToVG:%G)o"V%)M%:BV%s"VF4"%@)9u:o)G%MF)3%u%3)To@V%'V*o9V%uG'%9)3~uFoG8%o:%Xo:B%:BV%FV9)F'oG8%)M%:BV%u3ToVG:%G)o"V%MF)3%:BV%9)3~s:VF%oG%:BV%"u3V%F))3%oG%XBo9B%:BV%s"VF%o"%:F]oG8%:)%us:BVG:o9u:Vv%)GV%o"%uT@V%:)%Bu*V%uG%VMMV9:o*V%"V9)G'%Mu9:)F%)M%us:BVG:o9u:o)G!afeW%lBo"a9@uFoMo9u:o)G%GVV'V'W%u@")%FV's9V"%:BV%u3)sG:%)M%:o3V%uG'%VMM)F:%GVV'V'%:)%9)3~@V:V%:BV%~F)9V""!a9o:u:o)G%GVV'V'W
jV8o"@u:o)G%uG'%FV8s@u:o)G

lBV%\u]3VG:%_uF'%JG's":F]%x\_J`%&u:u%RV9sFo:]%R:uG'uF'v%FV|soFV3VG:%r!ev%FV|soFV"%:BV%s"V%)M%H?N%M)F%u@@%FV3):V%GV:X)FQ%u99V""%:Bu:%)Fo8oGu:V"%MF)3%)s:"o'V%:BV%GV:X)FQ%:)%u%_uF'%&u:u%{G*oF)G3VG:%x_&{`!af<W%;V8oGGoG8%Xo:B%\_JU&RR%*VF"o)G%e!fv%:BV%s"V%)M%H?N%o"%FV|soFV'%M)F%u@@%u'3oGo":Fu:o*V%u99V""%:)%:BV%_&{v%V*VG%oM%:BV%s"VF%o"%Xo:BoG%u%:Fs":V'%GV:X)FQ!af}W
{sF)~VuG%+Go)G

lBV%"V9)G'%\u]3VG:%RVF*o9V"%&oFV9:o*V%FV|soFV"%q":F)G8%9s":)3VF%us:BVG:o9u:o)Gq%)G%3)":%V@V9:F)Go9%~u]3VG:"%oG%:BV%{sF)~VuG%{9)G)3o9%NFVu%"oG9V%RV~:V3TVF%P<v%f#Pm!a9o:u:o)G%GVV'V'W
JG'ou

JG%JG'ouv%:BV%dV"VF*V%;uGQ%)M%JG'ou%3uG'u:V'%:X)UMu9:)F%us:BVG:o9u:o)G%M)F%u@@%)G@oGV%:FuG"u9:o)G"%3u'V%s"oG8%u%'VTo:%)F%9FV'o:%9uF'%s"oG8%Vo:BVF%u%~u""X)F'%)F%u%)GVU:o3V%~u""X)F'%"VG:%)*VF%RHR!%lBo"%Xu"%:V3~)FuFo@]%Xo:B'FuXG%oG%f#Pw%M)F%:FuG"u9:o)G"%s~%:)%fv###%oG%:BV%XuQV%)M%:BV%k)*V3TVF%f#Pw%TuGQG):V%'V3)GV:o"u:o)G!%pVG')F"%"s9B%u"%+TVF%Bu*V%TVVG%~s@@V'%s~%T]%:BV%9VG:Fu@%TuGQ%M)F%u@@)XoG8%:FuG"u9:o)G"%:)%:uQV%~@u9V%Xo:B)s:%:X)UMu9:)F%us:BVG:o9u:o)G!afwWafiW
+Go:V'%R:u:V"

&V:uo@"%M)F%us:BVG:o9u:o)G%M)F%?V'VFu@%{3~@)]VV"%uG'%_)G:Fu9:)F"%oG%:BV%+RN%uFV%'VMoGV'%Xo:B%:BV%/)3V@uG'%RV9sFo:]%\FV"o'VG:ou@%&oFV9:o*V%Pf%x/R\&UPf`!afrW

{(o":oG8%us:BVG:o9u:o)G%3V:B)')@)8oV"%oG*)@*V%:BV%V(~@uoGV'%:BFVV%:]~V"%)M%Tu"o9%qMu9:)F"q!%Ns:BVG:o9u:o)G%3V:B)'"%:Bu:%'V~VG'%)G%3)FV%:BuG%)GV%Mu9:)F%uFV%3)FV%'oMMo9s@:%:)%9)3~F)3o"V%:BuG%"oG8@VUMu9:)F%3V:B)'"!a9o:u:o)G%GVV'V'WafmW

Jl%FV8s@u:)F]%":uG'uF'"%M)F%u99V""%:)%?V'VFu@%b)*VFG3VG:%"]":V3"%FV|soFV%:BV%s"V%)M%3s@:oUMu9:)F%us:BVG:o9u:o)G%:)%u99V""%"VG"o:o*V%Jl%FV")sF9V"v%M)F%V(u3~@V%XBVG%@)88oG8%)G%:)%GV:X)FQ%'V*o9V"%:)%~VFM)F3%u'3oGo":Fu:o*V%:u"Q"ae#W%uG'%XBVG%u99V""oG8%uG]%9)3~s:VF%s"oG8%u%~Fo*o@V8V'%@)8oG!aePW

kJRl%R~V9ou@%\sT@o9u:o)G%r##UweUe%'o"9s""V"%*uFo)s"%M)F3"%)M%:X)UMu9:)F%us:BVG:o9u:o)G%uG'%~F)*o'V"%8so'uG9V%)G%s"oG8%:BV3%oG%Ts"oGV""%~F)9V""V"%FV|soFoG8%'oMMVFVG:%@V*V@"%)M%u""sFuG9V!aefW

JG%f##}v%:BV%+Go:V'%R:u:V"4%?V'VFu@%?oGuG9ou@%JG":o:s:o)G"%{(u3oGu:o)G%_)sG9o@%o""sV'%8so'uG9V%M)F%MoGuG9ou@%oG":o:s:o)G"%FV9)33VG'oG8%MoGuG9ou@%oG":o:s:o)G"%9)G's9:%Fo"QUTu"V'%u""V""3VG:"v%V*u@su:V%9s":)3VF%uXuFVGV""%~F)8Fu3"v%uG'%'V*V@)~%"V9sFo:]%3Vu"sFV"%:)%FV@ouT@]%us:BVG:o9u:V%9s":)3VF"%FV3):V@]%u99V""oG8%)G@oGV%MoGuG9ou@%"VF*o9V"v%)MMo9ou@@]%FV9)33VG'oG8%:BV%s"V%)M%us:BVG:o9u:o)G%3V:B)'"%:Bu:%'V~VG'%)G%3)FV%:BuG%)GV%Mu9:)F%x"~V9oMo9u@@]v%XBu:%u%s"VF%QG)X"v%Bu"v%uG'%o"`%:)%'V:VF3oGV%:BV%s"VF4"%o'VG:o:]!aeeW%JG%FV"~)G"V%:)%:BV%~sT@o9u:o)Gv%Gs3VF)s"%us:BVG:o9u:o)G%*VG')F"%TV8uG%o3~F)~VF@]%~F)3):oG8%9Bu@@VG8VU|sV":o)G"v%"V9FV:%o3u8V"v%uG'%):BVF%QG)X@V'8VUTu"V'%3V:B)'"%u"%q3s@:oUMu9:)Fq%us:BVG:o9u:o)G!%&sV%:)%:BV%FV"s@:oG8%9)GMs"o)G%uG'%Xo'V"~FVu'%u')~:o)G%)M%"s9B%3V:B)'"v%)G%Ns8s":%P}v%f##wv%:BV%??J{_%~sT@o"BV'%"s~~@V3VG:u@%8so'V@oGV"XBo9B%":u:V"%:Bu:%T]%'VMoGo:o)Gv%u%q:FsVq%3s@:oUMu9:)F%us:BVG:o9u:o)G%"]":V3%3s":%s"V%'o":oG9:%oG":uG9V"%)M%:BV%:BFVV%Mu9:)F"%)M%us:BVG:o9u:o)G%o:%Bu'%'VMoGV'v%uG'%G):%0s":%s"V%3s@:o~@V%oG":uG9V"%)M%u%"oG8@V%Mu9:)F!ae<W
RV9sFo:]

N99)F'oG8%:)%~F)~)GVG:"v%3s@:oUMu9:)F%us:BVG:o9u:o)G%9)s@'%'Fu":o9u@@]%FV's9V%:BV%oG9o'VG9V%)M%)G@oGV%o'VG:o:]%:BVM:%uG'%):BVF%)G@oGV%MFus'v%TV9us"V%:BV%*o9:o34"%~u""X)F'%X)s@'%G)%@)G8VF%TV%VG)s8B%:)%8o*V%u%:BoVM%~VF3uGVG:%u99V""%:)%:BVoF%oGM)F3u:o)G!%/)XV*VFv%3uG]%3s@:oUMu9:)F%us:BVG:o9u:o)G%u~~F)u9BV"%FV3uoG%*s@GVFuT@V%:)%~Bo"BoG8vae}W%3uGUoGU:BVUTF)X"VFv%uG'%3uGUoGU:BVU3o''@V%u::u9Q"!aewW%lX)UMu9:)F%us:BVG:o9u:o)G%oG%XVT%u~~@o9u:o)G"%uFV%V"~V9ou@@]%"s"9V~:oT@V%:)%~Bo"BoG8%u::u9Q"v%~uF:o9s@uF@]%oG%RHR%uG'%VU3uo@"v%uG'v%u"%u%FV"~)G"Vv%3uG]%V(~VF:"%u'*o"V%s"VF"%G):%:)%"BuFV%:BVoF%*VFoMo9u:o)G%9)'V"%Xo:B%uG])GVvaeiW%uG'%3uG]%XVT%u~~@o9u:o)G%~F)*o'VF"%Xo@@%~@u9V%uG%u'*o")F]%oG%uG%VU3uo@%)F%RHR%9)G:uoGoG8%u%9)'V!aerW

Hs@:oUMu9:)F%us:BVG:o9u:o)G%3u]%TV%oGVMMV9:o*VaemW%u8uoG":%3)'VFG%:BFVu:"v%@oQV%NlH%"Qo33oG8v%~Bo"BoG8v%uG'%3u@XuFV!a<#W

JG%Hu]%f#Pi%Df%lV@VMGo9uv%u%bVF3uG%3)To@V%"VF*o9V%~F)*o'VFv%9)GMoF3V'%:Bu:%9]TVF9Fo3oGu@"%Bu'%V(~@)o:V'%RRi%*s@GVFuTo@o:oV"%:)%T]~u""%RHR%Tu"V'%:X)U":V~%us:BVG:o9u:o)G%:)%')%sGus:B)Fo6V'%Xo:B'FuXu@"%MF)3%s"VF"%TuGQ%u99)sG:"!%lBV%9Fo3oGu@"%MoF":%oGMV9:V'%:BV%u99)sG:%B)@'VF4"%9)3~s:VF"%oG%uG%u::V3~:%:)%":Vu@%:BVoF%TuGQ%u99)sG:%9FV'VG:ou@"%uG'%~B)GV%Gs3TVF"!%lBVG%:BV%u::u9QVF"%~sF9Bu"V'%u99V""%:)%u%MuQV%:V@V9)3%~F)*o'VF%uG'%"V:Us~%u%FV'oFV9:%M)F%:BV%*o9:o34"%~B)GV%Gs3TVF%:)%u%BuG'"V:%9)G:F)@@V'%T]%:BV3!%?oGu@@]%:BV%u::u9QVF"%@)88V'%oG:)%*o9:o3"4%)G@oGV%TuGQ%u99)sG:"%uG'%FV|sV":V'%M)F%:BV%3)GV]%)G%:BV%u99)sG:"%:)%TV%Xo:B'FuXG%:)%u99)sG:"%)XGV'%T]%:BV%9Fo3oGu@"!%RHR%~u""9)'V"%XVFV%F)s:V'%:)%~B)GV%Gs3TVF"%9)G:F)@@V'%T]%:BV%u::u9QVF"%uG'%:BV%9Fo3oGu@"%:FuG"MVFFV'%:BV%3)GV]%)s:!a<PW
J3~@V3VG:u:o)G

HuG]%3s@:oUMu9:)F%us:BVG:o9u:o)G%~F)'s9:"%FV|soFV%s"VF"%:)%'V~@)]%9@oVG:%")M:XuFV%:)%3uQV%3s@:oUMu9:)F%us:BVG:o9u:o)G%"]":V3"%X)FQ!%R)3V%*VG')F"%Bu*V%9FVu:V'%"V~uFu:V%oG":u@@u:o)G%~u9Qu8V"%M)F%GV:X)FQ%@)8oGv%>VT%u99V""%9FV'VG:ou@"%uG'%p\k%9)GGV9:o)G%9FV'VG:ou@"!%?)F%"s9B%~F)'s9:"v%:BVFV%3u]%TV%M)sF%)F%Mo*V%'oMMVFVG:%")M:XuFV%~u9Qu8V"%:)%~s"B%')XG%:)%:BV%9@oVG:%\_%oG%)F'VF%:)%3uQV%s"V%)M%:BV%:)QVG%)F%"3uF:%9uF'!%lBo"%:FuG"@u:V"%:)%M)sF%)F%Mo*V%~u9Qu8V"%)G%XBo9B%*VF"o)G%9)G:F)@%Bu"%:)%TV%~VFM)F3V'v%uG'%M)sF%)F%Mo*V%~u9Qu8V"%:)%9BV9Q%M)F%9)GM@o9:"%Xo:B%Ts"oGV""%u~~@o9u:o)G"!%JM%u99V""%9uG%TV%)~VFu:V'%s"oG8%XVT%~u8V"v%o:%o"%~)""oT@V%:)%@o3o:%:BV%)*VFBVu'"%)s:@oGV'%uT)*V%:)%u%"oG8@V%u~~@o9u:o)G!%>o:B%):BVF%3s@:oUMu9:)F%us:BVG:o9u:o)G%")@s:o)G"v%"s9B%u"%q*oF:su@q%:)QVG"%uG'%")3V%BuF'XuFV%:)QVG%~F)'s9:"v%G)%")M:XuFV%3s":%TV%oG":u@@V'%T]%VG'%s"VF"!

lBVFV%uFV%'FuXTu9Q"%:)%3s@:oUMu9:)F%us:BVG:o9u:o)G%:Bu:%uFV%QVV~oG8%3uG]%u~~F)u9BV"%MF)3%TV9)3oG8%Xo'V"~FVu'!%R)3V%s"VF"%Bu*V%'oMMo9s@:]%QVV~oG8%:Fu9Q%)M%u%BuF'XuFV%:)QVG%)F%+R;%~@s8!%HuG]%s"VF"%')%G):%Bu*V%:BV%:V9BGo9u@%"Qo@@"%GVV'V'%:)%oG":u@@%u%9@oVG:U"o'V%")M:XuFV%9VF:oMo9u:V%T]%:BV3"V@*V"!%bVGVFu@@]v%3s@:oUMu9:)F%")@s:o)G"%FV|soFV%u''o:o)Gu@%oG*V":3VG:%M)F%o3~@V3VG:u:o)G%uG'%9)":"%M)F%3uoG:VGuG9V!%H)":%BuF'XuFV%:)QVGUTu"V'%"]":V3"%uFV%~F)~FoV:uF]%uG'%")3V%*VG')F"%9BuF8V%uG%uGGsu@%MVV%~VF%s"VF!%&V~@)]3VG:%)M%BuF'XuFV%:)QVG"%o"%@)8o":o9u@@]%9Bu@@VG8oG8!%/uF'XuFV%:)QVG"%3u]%8V:%'u3u8V'%)F%@)":%uG'%o""suG9V%)M%:)QVG"%oG%@uF8V%oG's":FoV"%"s9B%u"%TuGQoG8%)F%V*VG%Xo:BoG%@uF8V%VG:VF~Fo"V"%GVV'"%:)%TV%3uGu8V'!%JG%u''o:o)G%:)%'V~@)]3VG:%9)":"v%3s@:oUMu9:)F%us:BVG:o9u:o)G%)M:VG%9uFFoV"%"o8GoMo9uG:%u''o:o)Gu@%"s~~)F:%9)":"!%N%f##r%"sF*V]a<fW%)M%)*VF%Pf#%+!%R!%9FV'o:%sGo)G"%T]%:BV%_FV'o:%+Go)G%C)sFGu@%FV~)F:V'%)G%:BV%"s~~)F:%9)":"%u"")9ou:V'%Xo:B%:X)UMu9:)F%us:BVG:o9u:o)G!%JG%:BVoF%FV~)F:v%")M:XuFV%9VF:oMo9u:V"%uG'%")M:XuFV%:))@TuF%u~~F)u9BV"%XVFV%FV~)F:V'%:)%Bu*V%:BV%Bo8BV":%"s~~)F:%9)":"!

dV"VuF9B%oG:)%'V~@)]3VG:"%)M%3s@:oUMu9:)F%us:BVG:o9u:o)G%"9BV3V"a<eW%Bu"%"B)XG%:Bu:%)GV%)M%:BV%V@V3VG:"%:Bu:%:VG'"%:)%o3~u9:%:BV%u')~:o)G%)M%"s9B%"]":V3"%o"%:BV%@oGV%)M%Ts"oGV""%)M%:BV%)F8uGo6u:o)G%:Bu:%'V~@)]"%:BV%3s@:oUMu9:)F%us:BVG:o9u:o)G%"]":V3!%{(u3~@V"%9o:V'%oG9@s'V%:BV%+!%R!%MV'VFu@%8)*VFG3VG:v%XBo9B%V3~@)]"%uG%V@uT)Fu:V%"]":V3%)M%~B]"o9u@%:)QVG"%xXBo9B%:BV3"V@*V"%uFV%Tu9QV'%T]%F)Ts":%\sT@o9%.V]%JGMFu":Fs9:sFV`v%u"%XV@@%u"%~Fo*u:V%TuGQ"v%XBo9B%:VG'%:)%~FVMVF%3s@:oUMu9:)F%us:BVG:o9u:o)G%"9BV3V"%M)F%:BVoF%9s":)3VF"%:Bu:%oG*)@*V%3)FV%u99V""oT@Vv%@V""%V(~VG"o*V%3VuG"%)M%o'VG:o:]%*VFoMo9u:o)Gv%"s9B%u"%uG%u~~%oG":u@@V'%)G:)%u%9s":)3VFU)XGV'%"3uF:~B)GV!%&V"~o:V%:BV%*uFou:o)G"%:Bu:%V(o":%u3)G8%u*uo@uT@V%"]":V3"%:Bu:%)F8uGo6u:o)G"%3u]%Bu*V%:)%9B))"V%MF)3v%)G9V%u%3s@:oUMu9:)F%us:BVG:o9u:o)G%"]":V3%o"%'V~@)]V'%Xo:BoG%uG%)F8uGo6u:o)Gv%o:%:VG'"%:)%FV3uoG%oG%~@u9Vv%u"%s"VF"%oG*uFouT@]%u99@o3u:V%:)%:BV%~FV"VG9V%uG'%s"V%)M%:BV%"]":V3%uG'%V3TFu9V%o:%)*VF%:o3V%u"%u%G)F3u@o6V'%V@V3VG:%)M%:BVoF%'uo@]%~F)9V""%)M%oG:VFu9:o)G%Xo:B%:BVoF%FV@V*uG:%oGM)F3u:o)G%"]":V3!

>Bo@V%:BV%~VF9V~:o)G%o"%:Bu:%3s@:oUMu9:)F%us:BVG:o9u:o)G%o"%Xo:BoG%:BV%FVu@3%)M%~VFMV9:%"V9sFo:]v%d)8VF%bFo3V"%XFo:V"a<<W%:Bu:%oM%G):%~F)~VF@]%o3~@V3VG:V'%uG'%9)GMo8sFV'v%3s@:oUMu9:)F%us:BVG:o9u:o)G%9uG%oG%Mu9:%TV%Vu"o@]%'VMVu:V'!
\u:VG:"

JG%f#Pev%.o3%&):9)3%9@uo3V'%:)%Bu*V%oG*VG:V'%:X)UMu9:)F%us:BVG:o9u:o)G%oG%u%f###%~u:VG:va<}W%uG'%TFoVM@]%:BFVu:VGV'%:)%"sV%u@@%:BV%3u0)F%XVT%"VF*o9V"!%/)XV*VFv%:BV%{sF)~VuG%\u:VG:%DMMo9V%FV*)QV'%Bo"%~u:VG:a<wW%oG%@o8B:%)M%uG%VuF@oVF%Pmmr%+R%~u:VG:%BV@'%T]%NlLl!a<iW
{(u3~@V"
RV*VFu@%~)~s@uF%XVT%"VF*o9V"%V3~@)]%3s@:oUMu9:)F%us:BVG:o9u:o)Gv%s"su@@]%u"%uG%)~:o)Gu@%MVu:sFV%:Bu:%o"%'Vu9:o*u:V'%T]%'VMus@:!a<rW%HuG]%JG:VFGV:%"VF*o9V"%xu3)G8%:BV3%b))8@V%uG'%N3u6)G%N>R`%s"V%:BV%)~VG%lo3VUTu"V'%)GVU:o3V%~u""X)F'%u@8)Fo:B3%xlDl\`%:)%"s~~)F:%:X)U":V~%us:BVG:o9u:o)G!%
"""

print("--- Decrypting with Substitution Map ---")
solve_substitution(ciphertext)
