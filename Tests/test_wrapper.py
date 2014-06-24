__author__ = 'Apollo117'
import pytest
import SpiceyPy as spice
import numpy as np
import numpy.testing as npt


def test_appndc():
    assert 1


def test_appndd():
    assert 1


def test_appndi():
    assert 1


def test_axisar():
    assert 1


def test_b1900():
    assert spice.b1900() == 2415020.31352


def test_b1950():
    assert spice.b1950() == 2433282.42345905


def test_badkpv():
    assert 1


def test_bodc2n():
    assert 1


def test_bodc2s():
    assert 1


def test_boddef():
    assert 1


def test_bodfnd():
    assert 1


def test_bodn2c():
    assert 1


def test_bods2c():
    assert 1


def test_bodvar():
    assert 1


def test_bodvcd():
    assert 1


def test_bodvrd():
    assert 1


def test_brcktd():
    assert 1


def test_brckti():
    assert 1


def test_bschoc():
    assert 1


def test_bschoi():
    assert 1


def test_bsrchc():
    assert 1


def test_bsrchd():
    assert 1


def test_bsrchi():
    assert 1


def test_card():
    assert 1


def test_cgv2el():
    assert 1


def test_chkin():
    assert 1


def test_chkout():
    assert 1


def test_cidfrm():
    assert 1


def test_ckcls():
    assert 1


def test_ckcov():
    assert 1


def test_ckgp():
    assert 1


def test_ckgpav():
    assert 1


def test_cklpf():
    assert 1


def test_ckobj():
    assert 1


def test_ckopn():
    assert 1


def test_ckupf():
    assert 1


def test_ckw01():
    assert 1


def test_ckw02():
    assert 1


def test_ckw03():
    assert 1


def test_ckw05():
    assert 1


def test_clight():
    assert spice.clight() == 299792.458


def test_clpool():
    assert 1


def test_cmprss():
    assert 1


def test_cnmfrm():
    assert 1


def test_conics():
    assert 1


def test_convrt():
    assert 1


def test_copy():
    assert 1


def test_cpos():
    assert 1


def test_cposr():
    assert 1


def test_cvpool():
    assert 1


def test_cyllat():
    assert 1


def test_cylrec():
    assert 1


def test_cylsph():
    a = np.array(spice.cylsph(1.0, np.deg2rad(180.0), 1.0))
    b = np.array([1.4142, np.deg2rad(180.0), np.deg2rad(45.0)])
    np.testing.assert_almost_equal(b, a, decimal=4)


def test_dafac():
    assert 1


def test_dafbbs():
    assert 1


def test_dafbfs():
    assert 1


def test_dafcls():
    assert 1


def test_dafcs():
    assert 1


def test_dafdc():
    assert 1


def test_dafec():
    assert 1


def test_daffna():
    assert 1


def test_daffpa():
    assert 1


def test_dafgda():
    assert 1


def test_dafgn():
    assert 1


def test_dafgs():
    assert 1


def test_dafgsr():
    assert 1


def test_dafopr():
    assert 1


def test_dafopw():
    assert 1


def test_dafps():
    assert 1


def test_dafrda():
    assert 1


def test_dafrfr():
    assert 1


def test_dafrs():
    assert 1


def test_dafus():
    assert 1


def test_dasac():
    assert 1


def test_dascls():
    assert 1


def test_dasec():
    assert 1


def test_dasopr():
    assert 1


def test_dcyldr():
    assert 1


def test_deltet():
    assert 1


def test_det():
    assert 1


def test_dgeodr():
    assert 1


def test_diags2():
    assert 1


def test_diff():
    assert 1


def test_dlatdr():
    assert 1


def test_dp2hx():
    assert 1


def test_dpgrdr():
    assert 1


def test_dpmax():
    assert 1


def test_dpmin():
    assert 1


def test_dpr():
    assert spice.dpr() == 180.0 / np.arccos(-1.0)


def test_drdcyl():
    assert 1


def test_drdgeo():
    assert 1


def test_drdlat():
    assert 1


def test_drdpgr():
    assert 1


def test_drdsph():
    assert 1


def test_dsphdr():
    assert 1


def test_dtpool():
    assert 1


def test_ducrss():
    assert 1


def test_dvcrss():
    assert 1


def test_dvdot():
    assert 1


def test_dvhat():
    assert 1


def test_dvnorm():
    assert 1


def test_dvpool():
    assert 1


def test_dvsep():
    assert 1


def test_edlimb():
    assert 1


def test_ekacec():
    assert 1


def test_ekaced():
    assert 1


def test_ekacei():
    assert 1


def test_ekaclc():
    assert 1


def test_ekacld():
    assert 1


def test_ekacli():
    assert 1


def test_ekappr():
    assert 1


def test_ekbseg():
    assert 1


def test_ekccnt():
    assert 1


def test_ekcii():
    assert 1


def test_ekcls():
    assert 1


def test_ekdelr():
    assert 1


def test_ekffld():
    assert 1


def test_ekfind():
    assert 1


def test_ekgc():
    assert 1


def test_ekgd():
    assert 1


def test_ekgi():
    assert 1


def test_ekifld():
    assert 1


def test_ekinsr():
    assert 1


def test_eklef():
    assert 1


def test_eknelt():
    assert 1


def test_eknseg():
    assert 1


def test_ekntab():
    assert 1


def test_ekopn():
    assert 1


def test_ekopr():
    assert 1


def test_ekops():
    assert 1


def test_ekopw():
    assert 1


def test_ekpsel():
    assert 1


def test_ekrcec():
    assert 1


def test_ekrced():
    assert 1


def test_ekrcei():
    assert 1


def test_ekssum():
    assert 1


def test_ektnam():
    assert 1


def test_ekucec():
    assert 1


def test_ekuced():
    assert 1


def test_ekucei():
    assert 1


def test_ekuef():
    assert 1


def test_el2cgv():
    assert 1


def test_elemc():
    assert 1


def test_elemd():
    assert 1


def test_elemi():
    assert 1


def test_eqstr():
    assert spice.eqstr("A short string    ", "ashortstring")
    assert spice.eqstr("Embedded        blanks", "Em be dd ed bl an ks")
    assert spice.eqstr("One word left out", "WORD LEFT OUT") is False


def test_erract():
    assert 1


def test_errch():
    assert 1


def test_errdev():
    assert 1


def test_errdp():
    assert 1


def test_errint():
    assert 1


def test_errprt():
    assert 1


def test_esrchc():
    assert 1


def test_et2lst():
    assert 1


def test_et2utc():
    assert 1


def test_etcal():
    assert 1


def test_eul2m():
    assert 1


def test_eul2xf():
    assert 1


def test_exists():
    assert 1


def test_expool():
    assert 1


def test_failed():
    assert 1


def test_frame():
    assert 1


def test_frinfo():
    assert 1


def test_frmnam():
    assert 1


def test_ftncls():
    assert 1


def test_furnsh():
    assert 1


def test_gcpool():
    assert 1


def test_gdpool():
    assert 1


def test_georec():
    assert 1


def test_getcml():
    assert 1


def test_getelm():
    assert 1


def test_getfat():
    assert 1


def test_getfov():
    assert 1


def test_getmsg():
    assert 1


def test_gfbail():
    assert 1


def test_gfclrh():
    assert 1


def test_gfdist():
    assert 1


def test_gfevnt():
    assert 1


def test_gffove():
    assert 1


def test_gfinth():
    assert 1


def test_gfocce():
    assert 1


def test_gfoclt():
    assert 1


def test_gfposc():
    assert 1


def test_gfrefn():
    assert 1


def test_gfrepf():
    assert 1


def test_gfrepi():
    assert 1


def test_gfrepu():
    assert 1


def test_gfrfov():
    assert 1


def test_gfrr():
    assert 1


def test_gfsep():
    assert 1


def test_gfsntc():
    assert 1


def test_gfsstp():
    assert 1


def test_gfstep():
    assert 1


def test_gfsubc():
    assert 1


def test_gftfov():
    assert 1


def test_gfuds():
    assert 1


def test_gipool():
    assert 1


def test_gnpool():
    assert 1


def test_halfpi():
    assert spice.halfpi() == np.pi / 2


def test_hx2dp():
    assert 1


def test_ident():
    assert 1


def test_illum():
    assert 1


def test_ilumin():
    assert 1


def test_inedpl():
    assert 1


def test_inelpl():
    assert 1


def test_inrypl():
    assert 1


def test_insrtc():
    assert 1


def test_insrtd():
    assert 1


def test_insrti():
    assert 1


def test_inter():
    assert 1


def test_intmax():
    assert 1


def test_intmin():
    assert 1


def test_invert():
    assert 1


def test_invort():
    assert 1


def test_isordv():
    assert 1


def test_isrchc():
    assert 1


def test_isrchd():
    assert 1


def test_isrchi():
    assert 1


def test_isrot():
    assert 1


def test_iswhsp():
    assert 1


def test_j1900():
    assert spice.j1900() == 2415020.0


def test_j1950():
    assert spice.j1950() == 2433282.5


def test_j2000():
    assert spice.j2000() == 2451545.0


def test_j2100():
    assert spice.j2100() == 2488070.0


def test_jyear():
    assert spice.jyear() == 31557600.0


def test_kclear():
    spice.kclear()
    assert spice.ktotal("ALL") == 0


def test_kdata():
    assert 1


def test_kinfo():
    assert 1


def test_ktotal():
    assert 1


def test_kxtrct():
    assert 1


def test_lastnb():
    assert 1


def test_latcyl():
    assert 1


def test_latrec():
    assert 1


def test_latsph():
    assert 1


def test_lcase():
    assert 1


def test_ldpool():
    assert 1


def test_lmpool():
    assert 1


def test_lparse():
    assert 1


def test_lparsm():
    assert 1


def test_lparss():
    assert 1


def test_lspcn():
    assert 1


def test_lstlec():
    assert 1


def test_lstled():
    assert 1


def test_lstlei():
    assert 1


def test_lstltc():
    assert 1


def test_lstltd():
    assert 1


def test_lstlti():
    assert 1


def test_ltime():
    assert 1


def test_lx4dec():
    assert 1


def test_lx4num():
    assert 1


def test_lx4sgn():
    assert 1


def test_lx4uns():
    assert 1


def test_lxqstr():
    assert 1


def test_m2eul():
    assert 1


def test_m2q():
    assert 1


def test_matchi():
    assert 1


def test_matchw():
    assert 1


def test_maxd():
    assert 1


def test_maxi():
    assert 1


def test_mequ():
    assert 1


def test_mequg():
    assert 1


def test_mind():
    assert 1


def test_mini():
    assert 1


def test_mtxm():
    assert 1


def test_mtxmg():
    assert 1


def test_mtxv():
    assert 1


def test_mtxvg():
    assert 1


def test_mxm():
    m1 = [[1.0, 1.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
    m2 = [[1.0, 0.0, 0.0], [0.0, 1.0, 1.0], [0.0, -1.0, 1.0]]
    mout = np.array(spice.mxm(m1, m2))
    m1 = np.array(m1)
    m2 = np.array(m2)
    mout2 = np.dot(m1, m2)
    assert np.array_equal(mout, mout2)


def test_mxmg():
    m1 = [[1.0, 4.0], [2.0, 5.0], [3.0, 6.0]]
    m2 = [[1.0, 2.0, 3.0], [2.0, 4.0, 6.0]]
    nrow1 = 3
    ncol1 = 2
    ncol2 = 3
    mout = np.array(spice.mxmg(m1, m2, nrow1, ncol1, ncol2))
    m1 = np.array(m1)
    m2 = np.array(m2)
    mout2 = np.dot(m1, m2)
    assert np.array_equal(mout, mout2)


def test_mxmt():
    assert 1


def test_mxmtg():
    assert 1


def test_mxv():
    assert 1


def test_mxvg():
    assert 1


def test_namfrm():
    assert 1


def test_ncpos():
    assert 1


def test_ncposr():
    assert 1


def test_nearpt():
    assert 1


def test_npedln():
    assert 1


def test_npelpt():
    assert 1


def test_nplnpt():
    assert 1


def test_nvc2pl():
    assert 1


def test_nvp2pl():
    assert 1


def test_ordc():
    assert 1


def test_ordd():
    assert 1


def test_ordi():
    assert 1


def test_orderc():
    assert 1


def test_orderd():
    assert 1


def test_orderi():
    assert 1


def test_oscelt():
    assert 1


def test_pckcov():
    assert 1


def test_pckfrm():
    assert 1


def test_pcklof():
    assert 1


def test_pckuof():
    assert 1


def test_pcpool():
    assert 1


def test_pdpool():
    assert 1


def test_pgrrec():
    assert 1


def test_pi():
    assert spice.pi() == np.pi


def test_pipool():
    assert 1


def test_pjelpl():
    assert 1


def test_pl2nvc():
    assert 1


def test_pl2nvp():
    assert 1


def test_pl2psv():
    assert 1


def test_pos():
    assert 1


def test_posr():
    assert 1


def test_prompt():
    assert 1


def test_prop2b():
    assert 1


def test_prsdp():
    assert spice.prsdp("-1. 000") == -1.0


def test_prsint():
    assert spice.prsint("PI") == 3


def test_psv2pl():
    assert 1


def test_putcml():
    assert 1


def test_pxform():
    assert 1


def test_q2m():
    assert 1


def test_qdq2av():
    assert 1


def test_qxq():
    assert 1


def test_radrec():
    assert 1


def test_rav2xf():
    assert 1


def test_raxisa():
    assert 1


def test_rdtext():
    assert 1


def test_reccyl():
    assert 1


def test_recgeo():
    assert 1


def test_reclat():
    assert 1


def test_recpgr():
    assert 1


def test_recrad():
    assert 1


def test_recsph():
    assert 1


def test_removc():
    assert 1


def test_removd():
    assert 1


def test_removi():
    assert 1


def test_reordc():
    assert 1


def test_reordd():
    assert 1


def test_reordi():
    assert 1


def test_reordl():
    assert 1


def test_repmc():
    assert 1


def test_repmct():
    assert 1


def test_repmd():
    assert 1


def test_repmf():
    assert 1


def test_repmi():
    assert 1


def test_repmot():
    assert 1


def test_reset():
    assert 1


def test_return():
    assert 1


def test_rotate():
    assert 1


def test_rotmat():
    assert 1


def test_rotvec():
    assert 1


def test_rpd():
    assert spice.rpd() == np.arccos(-1.0) / 180.0


def test_rquad():
    assert 1


def test_saelgv():
    assert 1


def test_scard():
    assert 1


def test_scdecd():
    assert 1


def test_sce2c():
    assert 1


def test_sce2s():
    assert 1


def test_sce2t():
    assert 1


def test_scencd():
    assert 1


def test_scfmt():
    assert 1


def test_scpart():
    assert 1


def test_scs2e():
    assert 1


def test_sct2e():
    assert 1


def test_sctiks():
    assert 1


def test_sdiff():
    assert 1


def test_set():
    assert 1


def test_setmsg():
    assert 1


def test_shellc():
    assert 1


def test_shelld():
    assert 1


def test_shelli():
    assert 1


def test_sigerr():
    assert 1


def test_sincpt():
    assert 1


def test_size():
    assert 1


def test_spd():
    assert spice.spd() == 86400.0


def test_sphcyl():
    assert 1


def test_sphlat():
    assert 1


def test_sphrec():
    assert 1


def test_spk14a():
    assert 1


def test_spk14b():
    assert 1


def test_spk14e():
    assert 1


def test_spkacs():
    assert 1


def test_spkapo():
    assert 1


def test_spkapp():
    assert 1


def test_spkaps():
    assert 1


def test_spkcls():
    assert 1


def test_spkcov():
    assert 1


def test_spkez():
    assert 1


def test_spkezp():
    assert 1


def test_spkezr():
    assert 1


def test_spkgeo():
    assert 1


def test_spkgps():
    assert 1


def test_spklef():
    assert 1


def test_spkltc():
    assert 1


def test_spkobj():
    assert 1


def test_spkopa():
    assert 1


def test_spkopn():
    assert 1


def test_spkpds():
    assert 1


def test_spkpos():
    assert 1


def test_spkssb():
    assert 1


def test_spksub():
    assert 1


def test_spkuds():
    assert 1


def test_spkuef():
    assert 1


def test_spkw02():
    assert 1


def test_spkw03():
    assert 1


def test_spkw05():
    assert 1


def test_spkw08():
    assert 1


def test_spkw09():
    assert 1


def test_spkw10():
    assert 1


def test_spkw12():
    assert 1


def test_spkw13():
    assert 1


def test_spkw15():
    assert 1


def test_spkw17():
    assert 1


def test_spkw18():
    assert 1


def test_srfrec():
    assert 1


def test_srfxpt():
    assert 1


def test_ssize():
    assert 1


def test_stelab():
    assert 1


def test_stpool():
    assert 1


def test_str2et():
    assert 1


def test_subpnt():
    assert 1


def test_subpt():
    assert 1


def test_subslr():
    assert 1


def test_subsol():
    assert 1


def test_sumad():
    assert 1


def test_sumai():
    assert 1


def test_surfnm():
    assert 1


def test_surfpt():
    assert 1


def test_surfpv():
    assert 1


def test_swpool():
    assert 1


def test_sxform():
    assert 1


def test_szpool():
    assert 1


def test_timdef():
    assert 1


def test_timout():
    assert 1


def test_tipbod():
    assert 1


def test_tisbod():
    assert 1


def test_tkvrsn():
    assert 1


def test_tparse():
    assert 1


def test_tpictr():
    assert 1


def test_trace():
    assert 1


def test_trcoff():
    assert 1


def test_tsetyr():
    assert 1


def test_twopi():
    assert spice.twopi() == np.pi * 2


def test_twovec():
    assert 1


def test_tyear():
    assert spice.tyear() == 31556925.9747


def test_ucase():
    assert 1


def test_ucrss():
    assert 1


def test_uddc():
    assert 1


def test_uddf():
    assert 1


def test_union():
    assert 1


def test_unitim():
    assert 1


def test_unload():
    assert 1


def test_unorm():
    assert spice.unorm([5.0, 12.0, 0.0]) == ([5/13, 12/13, 0.0], 13.0)


def test_unormg():
    assert 1


def test_utc2et():
    assert 1


def test_vadd():
    v1 = [1.0, 2.0, 3.0]
    v2 = [4.0, 5.0, 6.0]
    assert spice.vadd(v1, v2) == [5.0, 7.0, 9.0]


def test_vaddg():
    v1 = [1.0, 2.0, 3.0]
    v2 = [4.0, 5.0, 6.0]
    assert spice.vaddg(v1, v2, 3) == [5.0, 7.0, 9.0]


def test_valid():
    assert 1


def test_vcrss():
    assert 1


def test_vdist():
    assert 1


def test_vdistg():
    assert 1


def test_vdot():
    assert 1


def test_vdotg():
    assert 1


def test_vequ():
    assert 1


def test_vequg():
    assert 1


def test_vhat():
    assert 1


def test_vhatg():
    assert 1


def test_vlcom3():
    assert 1


def test_vlcom():
    assert 1


def test_vlcomg():
    assert 1


def test_vminug():
    assert 1


def test_vminus():
    assert 1


def test_vnorm():
    assert 1


def test_vnormg():
    assert 1


def test_vpack():
    assert 1


def test_vperp():
    assert 1


def test_vprjp():
    assert 1


def test_vprjpi():
    assert 1


def test_vproj():
    assert 1


def test_vrel():
    assert 1


def test_vrelg():
    assert 1


def test_vrotv():
    assert 1


def test_vscl():
    assert 1


def test_vsclg():
    assert 1


def test_vsep():
    assert 1


def test_vsepg():
    assert 1


def test_vsub():
    assert 1


def test_vsubg():
    assert 1


def test_vtmv():
    assert 1


def test_vtmvg():
    assert 1


def test_vupack():
    assert 1


def test_vzero():
    assert 1


def test_vzerog():
    assert 1


def test_wncard():
    assert 1


def test_wncomd():
    assert 1


def test_wncond():
    assert 1


def test_wndifd():
    assert 1


def test_wnelmd():
    assert 1


def test_wnexpd():
    assert 1


def test_wnextd():
    assert 1


def test_wnfetd():
    assert 1


def test_wnfild():
    assert 1


def test_wnfltd():
    assert 1


def test_wnincd():
    assert 1


def test_wninsd():
    assert 1


def test_wnintd():
    assert 1


def test_wnreld():
    assert 1


def test_wnsumd():
    assert 1


def test_wnunid():
    assert 1


def test_wnvald():
    assert 1


def test_xf2eul():
    assert 1


def test_xf2rav():
    assert 1


def test_xpose6():
    m1 = [[1.0, 2.0, 3.0, 4.0, 5.0, 6.0], [0.0, 7.0, 8.0, 9.0, 10.0, 11.0], [0.0, 0.0, 12.0, 13.0, 14.0, 15.0],
          [0.0, 0.0, 0.0, 16.0, 17.0, 18.0], [0.0, 0.0, 0.0, 0.0, 19.0, 20.0], [0.0, 0.0, 0.0, 0.0, 0.0, 21.0]]
    mout_expected = np.array(m1).transpose().tolist()
    assert spice.xpose6(m1) == mout_expected


def test_xpose():
    m1 = [[1.0, 2.0, 3.0], [0.0, 4.0, 5.0], [0.0, 6.0, 0.0]]
    assert spice.xpose(m1) == [[1.0, 0.0, 0.0], [2.0, 4.0, 6.0], [3.0, 5.0, 0.0]]
    assert spice.xpose(np.array(m1)) == [[1.0, 0.0, 0.0], [2.0, 4.0, 6.0], [3.0, 5.0, 0.0]]


def test_xposeg():
    m1 = [[1.0, 2.0, 3.0], [0.0, 4.0, 5.0], [0.0, 6.0, 0.0]]
    assert spice.xposeg(m1, 3, 3) == [[1.0, 0.0, 0.0], [2.0, 4.0, 6.0], [3.0, 5.0, 0.0]]
    assert spice.xposeg(np.array(m1), 3, 3) == [[1.0, 0.0, 0.0], [2.0, 4.0, 6.0], [3.0, 5.0, 0.0]]