name=input('Nama: ')
position=input('Jabatan: ')
salary=input('Gaji: ')
print('\n\n Nama:',name,'\n','Jabatan:',position,'\n','Gaji: Rp'+salary+',00 \n')
print('\n\n')
print('Pegawai dengan nama '+name+' dan jabatan '+position+' mendapat gaji sebesar Rp'+salary
	+',00 \ndan harus membayar pajak sebesar Rp'+str(int(int(salary)*(10/100)))+',00')
