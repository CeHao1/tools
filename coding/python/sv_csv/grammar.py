# read data
def read(self,readpath):
  f=open (readpath,'r')
  f_csv = csv.reader(f)
  i = 1
  for row0 in f_csv:
      if i > 1:
          row=list(map(lambda x: float(x), row0))
          self.course.append(row[course_i])
          self.X.append(row[X_i])
          self.Y.append(row[Y_i])
          #self.Vx.append(row[Vx_i])
          #self.kap.append(row[kap_i])
          self.psi.append(row[psi_i])
      else:
          course_i = row0.index('course')
          X_i = row0.index('X')
          Y_i = row0.index('Y')
          #Vx_i = row0.index('Vx')
          #kap_i = row0.index('kap')
          psi_i = row0.index('psi')

      i = i +1
  f.close()

# save data

# save title
f=open (os. getcwd()+'/savedata_Ce/MPCresults_'+track_name+'_'+car_name +save_name+'.csv','w')
f_csv = csv.writer(f)
sv = []
k = 0
for key in env.feature_keys:
    if isinstance(observations[0][int(k)],list):
        for i in range(3):
            sv.append(key+'_'+str(i))
    else:
        sv.append(key)

    k = k+1
    
sv.append('slip_angle_3')
sv.append('u_delta')
sv.append('u_a')
sv.append('u_thr')
sv.append('X')
sv.append('Y')
sv.append('psi')
sv.append('vx')
sv.append('vy')
sv.append('dpsi')
sv.append('ey')
sv.append('epsi')
sv.append('s')
f_csv.writerow(sv)


# save content
for ob,at,st,ey,epsi,s in zip(sum_ob,sum_act,sum_states,sum_ey,sum_epsi,sum_s):

    sv=[]
    for ele in ob[0]:
        if type(ele).__name__!='list':
            sv.append(ele)
        else:
            for sub in ele:
                  sv.append(sub)
    #sv.append(st.targetX)
    #sv.append(st.targetY)
    sv.append(at[0])
    sv.append(at[1])
    sv.append(at[2])

    for ele in st:
        if type(ele).__name__!='list':
            sv.append(ele)
        else:
            for sub in ele:
                sv.append(sub)
    
    sv.append(ey)
    sv.append(epsi)
    sv.append(s)
    f_csv.writerow(sv)
f.close()

print('-----------------------------------------------------------------')
print('------ File successfully saved ')
textmessage()
