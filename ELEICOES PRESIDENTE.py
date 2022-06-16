# -*- coding: utf-8 -*-
"""
Created on Wed May 18 15:46:54 2022

@author: djevs
"""

def main():
        
        
        
     lista=['LULA 13' , 'BOLSONARO 22' , 'CIRO GOMES 12' , 'BRANCO']
    
     try:
        numerocandidatos=int(input('ELEIÇÕES 2022 - DIGITE O NÚMERO DO SEU CANDIDATO, OU "0" PARA VOTAR EM BRANCO : '))
     except:
        print('') 
        print('COMANDO NÃO ACEITO. TENTE NOVAMENTE')
        return main()
     else:
        pass 
            
#CANDIDATOS INICIO    
        if numerocandidatos == 13:
                     
             print('')
             print('SE O SEU CANDIDATO É',lista[0]) 
             
             try:
              l=int(input('DIGITE 1 PARA CONFIRMAR OU "0" PARA RETORNAR : '))
             
              if l == 1:
                 print('VOTO COMPUTADO COM SUCESSO! - FIM')
                 return main()
              else:
                  print('TENTE NOVAMENTE')
                  return main()
             except: 
                 print('') 
                 print('COMANDO NÃO ACEITO. TENTE NOVAMENTE')
                 return main()
             
        
        elif numerocandidatos ==22: 
             print('')
             print('SE O SEU CANDIDATO É ' ,lista[1]) 
             try:
              b=int(input('DIGITE 1 PARA CONFIRMAR OU "0" PARA RETORNAR : '))
             except:
                 print('erro')
             if b == 1:
                 print('VOTO COMPUTADO COM SUCESSO! - FIM')
                 return main()
             else:
                 print('TENTE NOVAMENTE')
                 return main() 
        
        elif numerocandidatos ==12:
             print('')
             print('SE O SEU CANDIDATO É ' , lista[2])
             g=int(input('DIGITE 1 PARA CONFIRMAR OU "0" PARA VOLTAR : ')) 
             if g == 1:
                print('VOTO COMPUTADO COM SUCESSO ! - FIM') 
                return main()
             else:
                 print('TENTE NOVAMENTE')
                 return main()
#CANDIDATOS FIM         
#VOTOBRANCO INICIO         
        elif numerocandidatos ==0:
             print('')
             print('DESEJA VOTAR EM ' , lista[3] , '?')
             g=int(input('DIGITE 1 PARA CONFIRMAR OU "0" PARA VOLTAR : ')) 
             if g == 1:
                print('VOTO BRANCO COMPUTADO COM SUCESSO ! - FIM') 
                return main()
             else:
                 print('TENTE NOVAMENTE')
                 return main()
        elif numerocandidatos ==('enter'):
             print('')
             print('DESEJA VOTAR EM ' , lista[3] , '?')
             g=int(input('DIGITE 1 PARA CONFIRMAR OU "0" PARA VOLTAR : ')) 
             if g == 1:
                print('VOTO BRANCO COMPUTADO COM SUCESSO ! - FIM') 
                return main()
             else:
                 print('TENTE NOVAMENTE')
                 return main()     
#VOTOBRANCO FIM         
#VOTO NULO INICIO         
        else:
             
             anular=int(input('VOTO INVÁLIDO. PARA ANULAR DIGITE 1 , OU "0" PARA TENTAR  NOVAMENTE : '))
             if anular==1:
                print('VOTO ANULADO COM SUCESSO - FIM ')   
                return main()
             elif anular==0:
                 print('TENTE NOVAMENTE')
                 return main()
             else:
                 anular != 1 and 0
                 print('VOTO NÃO COMPUTADO, TENTE NOVAMENTE')
                 return main() 
#VOTO NULO FIM  







    
main()    