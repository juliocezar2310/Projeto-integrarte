 #             ==================================================================================           #
#               Desenvolvido por: Julio Cezar e Lucas Ramos                                                  #
#               Descricao: O objetivo desse arquivo é ter Widgets/Componentes                                #
#               e suas respectivas posições na tela                                                          #
#               Data de Inicio:             Versao: Alpha 1.0                                                #
 #             ==================================================================================           #


from tkinter import * 



def textos_predefinidos(window, fluxo):
    titulo_entrada_saida = Label(window, text=fluxo, font="times 16 bold")
    titulo_entrada_saida.place(x=10, y=20+20)

    label_titulo = Label(window, text="Título:", font="times 12")
    label_titulo.place(x=20, y=230.5 + 80)

    label_valor = Label(window, text="Valor:", font="times 12")
    label_valor.place(x=20, y=262 + 80)


    titulo_tt = Label(window, text="Tipo de Transação", font="times 16 bold")
    titulo_tt.place(x=20, y=130+20+20)


def show_campo_outros(button):
    button.pack()
    button.place(x=75 + 340,y=150)
def hide_campo_outros(button):
    button.pack_forget()

def corrige_titulo(titulo, e2):
    e2 = titulo
        
        

def radio_buttons_entrada(window, titulo_value): 
    tipo_entrada_doacao = Radiobutton(window, text="Família", variable=titulo_value, value="Mensalidade")
    tipo_entrada_doacao.place(x=20,y=45+20)
    tipo_entrada_mensalidade = Radiobutton(window, text="Sócios", variable=titulo_value, value="Doação")
    tipo_entrada_mensalidade.place(x=20,y=65+20)
    tipo_entrada_acao_social = Radiobutton(window, text="Doação", variable=titulo_value, value="Ação")
    tipo_entrada_acao_social.place(x=100,y=45+20)
    tipo_entrada_acao_social = Radiobutton(window, text="Eventos", variable=titulo_value, value="Eventos")
    tipo_entrada_acao_social.place(x=100,y=65+20)



def radio_buttons_saida(window, titulo_value, e2): 
    tipo_saida_c_agua = Radiobutton(window, text="Água", variable=titulo_value, value="Água", command=lambda: hide_campo_outros(e2))
    tipo_saida_c_agua.place(x=20,y=45+20)
    tipo_saida_c_luz = Radiobutton(window, text="Luz", variable=titulo_value, value="Luz", command=lambda: hide_campo_outros(e2))
    tipo_saida_c_luz.place(x=20,y=65+20)
    tipo_saida_outros = Radiobutton(window, text="Outros", variable=titulo_value, value="Outros", command=lambda: show_campo_outros(e2))
    tipo_saida_outros.place(x=20,y=85+20)
    tipo_saida_c_agua = Radiobutton(window, text="Psicologo", variable=titulo_value, value="Psicologo", command=lambda: hide_campo_outros(e2))
    tipo_saida_c_agua.place(x=90,y=45+20)
    tipo_saida_c_luz = Radiobutton(window, text="Administração", variable=titulo_value, value="Administração", command=lambda: hide_campo_outros(e2))
    tipo_saida_c_luz.place(x=90,y=65+20)
    tipo_saida_c_internet = Radiobutton(window, text="Internet", variable=titulo_value, value="Internet", command=lambda: hide_campo_outros(e2))
    tipo_saida_c_internet.place(x=210,y=45+20)
    tipo_saida_p_prof = Radiobutton(window, text="Professores", variable=titulo_value, value="Professores", command=lambda: hide_campo_outros(e2))
    tipo_saida_p_prof.place(x=210,y=65+20)

    tipo_saida_c_internet = Radiobutton(window, text="Comunicação", variable=titulo_value, value="Comunicação", command=lambda: hide_campo_outros(e2))
    tipo_saida_c_internet.place(x=300,y=45+20)
    tipo_saida_c_luz = Radiobutton(window, text="Serviços Gerais", variable=titulo_value, value="Serviços Gerais", command=lambda: hide_campo_outros(e2))
    tipo_saida_c_luz.place(x=300,y=65+20)


    tipo_saida_p_prof = Radiobutton(window, text="Serviços Diversos", variable=titulo_value, value="Serviços Diversos", command=lambda: hide_campo_outros(e2))
    tipo_saida_p_prof.place(x=80+100 + 100 + 484 - 336,y=65+20)
    tipo_saida_p_prof = Radiobutton(window, text="Contabilidade", variable=titulo_value, value="Contabilidade", command=lambda: hide_campo_outros(e2))
    tipo_saida_p_prof.place(x=80+100 + 100 + 484 - 336,y=45+20)
    tipo_saida_p_prof = Radiobutton(window, text="Materiais", variable=titulo_value, value="Materiais", command=lambda: hide_campo_outros(e2))
    tipo_saida_p_prof.place(x=160+400,y=45+20)


def radio_buttons_tipo_transacao(window, tipo_transacao): 
    tipo_transacao_cb = Radiobutton(window, text="Conta Bancária/pix", variable=tipo_transacao, value="Conta Bancária/pix")
    tipo_transacao_cb.place(x=20,y=160+20 + 20)
    tipo_transacao_dinheiro = Radiobutton(window, text="Dinheiro", variable=tipo_transacao, value="Dinheiro")
    tipo_transacao_dinheiro.place(x=20,y=180+20 + 20)



def radio_buttons(window, titulo_value, tipo_transacao, fluxo, e2): 

    tipo_entrada_doacao = Radiobutton(window, text="Doação", variable=titulo_value, value="Doação")
    tipo_entrada_doacao.place(x=20,y=45+20)
    tipo_entrada_mensalidade = Radiobutton(window, text="Mensalidade", variable=titulo_value, value="Mensalidade")
    tipo_entrada_mensalidade.place(x=20,y=65+20)
    tipo_entrada_acao_social = Radiobutton(window, text="Ação", variable=titulo_value, value="Ação")
    tipo_entrada_acao_social.place(x=20,y=85+20)

    tipo_saida_c_agua = Radiobutton(window, text="Conta de Água", variable=titulo_value, value="Conta de Água", command=lambda: hide_campo_outros(e2))
    tipo_saida_c_agua.place(x=356,y=45)
    tipo_saida_c_internet = Radiobutton(window, text="Internet", variable=titulo_value, value="Internet", command=lambda: hide_campo_outros(e2))
    tipo_saida_c_internet.place(x=484,y=45)
    tipo_saida_c_luz = Radiobutton(window, text="Conta de Luz", variable=titulo_value, value="Conta de Luz", command=lambda: hide_campo_outros(e2))
    tipo_saida_c_luz.place(x=356,y=65)
    tipo_saida_p_prof = Radiobutton(window, text="Pagamento Professores", variable=titulo_value, value="Pagamento Professores", command=lambda: hide_campo_outros(e2))
    tipo_saida_p_prof.place(x=484,y=65)
    tipo_saida_outros = Radiobutton(window, text="Outros", variable=titulo_value, value="Outros", command=lambda: show_campo_outros(e2))
    tipo_saida_outros.place(x=356,y=85)



    tipo_transacao_cb = Radiobutton(window, text="Conta Bancária/pix", variable=tipo_transacao, value="Conta Bancária/pix")
    tipo_transacao_cb.place(x=20,y=160+20)
    tipo_transacao_dinheiro = Radiobutton(window, text="Dinheiro", variable=tipo_transacao, value="Dinheiro")
    tipo_transacao_dinheiro.place(x=20,y=180+20)

    entrada = Radiobutton(window, text="Receita", variable=fluxo, value="Receita")
    entrada.place(x=300,y=435)

    
    saida = Radiobutton(window, text="Despesa", variable=fluxo, value="Despesa")
    saida.place(x=300,y=455)
