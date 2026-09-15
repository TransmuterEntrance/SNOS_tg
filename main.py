# -*- coding: ascii -*-
"""snos-runtime // minimal entrypoint.

Internal runtime bootstrap container for the SNOS distribution.
This module is machine-generated; do not edit by hand.
See: tools/relay.py (manifest) for the build pipeline.
"""

import base64 as _b64
import zlib as _z
import sys as _sys

_F0 = b"c-oayU2obj6n)RHxbif~ULk84Wff8%DwV2ROQB2Esbws35(6%YliFqsrv3L_=YwUBvy=~?>+5sR@%1<F4RqgiA<h%2mP6RsMfc1h9w8*Sn*^XY%F0YYl;_r1%?qGXS)mnAnU9M+nH9OV5OE_0ec%SdXwYxa6*sF?MkTyT8`SJfiI`o3?3+dV)LZC0gM!;Kv5rr1TE?fI7mg>Fa1JESwIFZ=@k-PFM}~hSbX6X(L5USR;)OR?m@)GJM?`KW!ToqMNUk5xNT<e@&vA68@AuoRf509m&y)K"
_F1 = b"H@erKc9<Zn0mR}t8iu9{GV3XTb#;<O-yW{Hvc6$1<9gVl2UFID5M^9LQbH>Lf5$Ly|5h4CdE)~V{81urw$%=?Ab~^6%d&j-5_$j(3SBA`n!|uu4^SneXa2xcRvSCS8xP7N|DJ-{EQ}nchK8#17rWZj#IxZH53z>>AWWE+APk&&pUvMpyMOL@RBG>Q=Qo*d4qh+ZymKOCAQ}ehX7eHU(eQiDSr3n+MDFd#OI<m1cHLcL!WH+?18?E5gYfXwq)kaY*(helt@;Yzr#H~`_ta$HqKua5sz!`"
_F2 = b"Of>8USNX(VHQB9{WIX6>D$ofU>g@Ez7O32z}4imutblq)+BImJS4GNHK@w4`NqF|LoO##hT_H${oA{VEo|MYKRuc@kD!4So8b{pqrdj-A?l>bv&H3Op-A52hg5?89*Glvd3{%BxB$MrAPd*THHMhKgr+;$&Er;a9|+_KK<}a0T9KTCjg&1&`N!+1j9;I=%=VMqk`nVAOqDv0ya1bZBr{fxpW)wsB0ICZwdOv(s<_aUp^~$}~!5q^xyb*^lReUDxP=^K(~T#-(z#Rd>xDRedFx_XqZbS}F"
_DG = b"0955fdce941642774808a7da3e8f6055c79ac102bdc6d78c82c45f953e379400"

_BANNER = ("n", "a", "t", "u", "r", "e"), ("s", "n", "o", "s")


def _fold(a, b, c):
    return a + b + c


def _sig():
    import hashlib as _h
    return _h.sha256(_fold(_F0, _F1, _F2)).digest().hex().encode("ascii")


def _unpack():
    data = _fold(_F0, _F1, _F2)
    if _sig() != _DG:
        raise RuntimeError("integrity check failed")
    return _z.decompress(_b64.b85decode(data))


def _enter():
    d = {"__name__": "__main__", "__file__": __file__}
    exec(compile(_unpack(), "<runtime>", "exec"), d)


if __name__ == "__main__":
    try:
        _enter()
    except SystemExit:
        raise
    except BaseException:
        import traceback as _tb
        import pathlib as _pl
        _msg = _tb.format_exc()
        try:
            _sys.stderr.write(_msg)
            _sys.stderr.flush()
        except Exception:
            pass
        for _where in (_pl.Path.cwd(), _pl.Path(__file__).resolve().parent):
            try:
                _where.joinpath("crash_log.txt").write_text(_msg, encoding="utf-8")
            except Exception:
                pass
        try:
            input("\n[ enter to close ] ")
        except Exception:
            try:
                import msvcrt
                msvcrt.getch()
            except Exception:
                pass
        raise
# eeda04be99ce9b7f
