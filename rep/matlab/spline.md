## integral
https://www.mathworks.com/help/matlab/ref/integral.html

## spline function
https://ww2.mathworks.cn/help/curvefit/referencelist.html?type=function&listtype=cat&category=splines&blocktype=all&capability=&s_tid=CRUX_lftnav

## curve integral
https://zhuanlan.zhihu.com/p/97430633


## plan spline
pp=csape(x, [k1 y k2],[o1 o2])  % k1 and k2 are boundary constraints, o1 and o2 are orders of constraints
dpp= fnder(pp,order)
path=ppval(pp, x)

### integral length
funh=@(u) sqrt(1+ppval(fnder(pp),u).^2);
L=integral(funh,low_bnd,up_bnd);
