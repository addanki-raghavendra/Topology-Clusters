#This function bins the entire histogram of the distance matrix (including double counting due to the symmetric matrix. 

def plot_total_partial_pdf(dd,dd11,dd12,dd22):

  hist, bin_edges=  np.histogram(dd,   bins=100, range=(2.0,3.50))
  hist11,bin_edges= np.histogram(dd11, bins=100, range=(2.0,3.50))
  hist12,bin_edges= np.histogram(dd12, bins=100, range=(2.0,3.50))
  hist22,bin_edges= np.histogram(dd22, bins=100, range=(2.0,3.50))
  fig,(ax,ax11,ax12,ax22)=plt.subplots(nrows=1,ncols=4)

  plt.title('Total and partial pair distribution functions',fontsize=20)
  ax.set_xlim(2,3.5) #Set limits for x-axisLegends                                       
  ax.set(title='total PDF',ylabel='Total PDF',xlabel='r')
  #ax.legend(loc='best')                                                                 
  ax.tick_params(axis='x', direction='inout',length=10)#Subplot Spacing                  
  ax.bar(bin_edges[:-1],hist, width=np.diff(bin_edges), ec="k",align="edge")
  ax11.set_xlim(2,3.5) #Set limits for x-axisLegends                                     
  ax11.set(title='S-S PDF',ylabel='PDF',xlabel='r')
  #ax11.legend(loc='best')                                                               
  ax11.tick_params(axis='x', direction='inout',length=10)#Subplot Spacing                
  ax12.set_xlim(2,3.5) #Set limits for x-axisLegends                                     
  ax12.set(title='Au-S PDF',ylabel='PDF',xlabel='r')
  #ax12.legend(loc='best')                                                               
  ax12.tick_params(axis='x', direction='inout',length=10)#Subplot Spacing                
  ax22.set_xlim(2,3.5) #Set limits for x-axisLegends                                     
  ax22.set(title='Au-Au PDF',ylabel='PDF',xlabel='r')
  #ax22.legend(loc='best')                                                               

  ax22.tick_params(axis='x', direction='inout',length=10)#Subplot Spacing                
  ax11.bar(bin_edges[:-1],hist11, width=np.diff(bin_edges),ec="k",align="edge")
  ax12.bar(bin_edges[:-1],hist12, width=np.diff(bin_edges),ec="k",align="edge")
  ax22.bar(bin_edges[:-1],hist22, width=np.diff(bin_edges),ec="k",align="edge")
  plt.tight_layout()
  plt.savefig('foo.png')
  plt.show()
  return
