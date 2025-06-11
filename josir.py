# Função que simula IA para gerar sugestão de look
def gerar_look_com_ia(ocasião, estilo, clima, humor, tempo_fora, locomocao, calçado, vibe_cor, acessorios):
    descricao = f"""
    Pensando em um look para {ocasião}, no clima {clima}, com você se sentindo {humor.lower()}, 
    preferindo o estilo {estilo.lower()}, e com previsão de passar {tempo_fora.lower()} fora de casa, indo de {locomocao.lower()}, 
    usando {calçado.lower()} e com vibe de cor {vibe_cor.lower()}...
    """
    look_final = ""

    if estilo == "Básico":
        look_final = "uma calça jeans confortável, camiseta branca e tênis"
    elif estilo == "Fashionista":
        look_final = "uma saia midi estampada, top estiloso e sandália com salto bloco"
    elif estilo == "Esportivo":
        look_final = "um conjunto de moletom estiloso com tênis chunky e pochete"
    elif estilo == "Romântico":
        look_final = "um vestido floral com sandália delicada e bolsa pequena"
    elif estilo == "Despojado":
        look_final = "uma jardineira jeans, cropped descolado e tênis"

    if clima == "Frio":
        look_final += " + uma jaqueta para se proteger do frio"
    elif clima == "Chuvoso":
        look_final += " + uma capa estilosa ou trench coat com guarda-chuva"

    acessorios_texto = ""
    if acessorios != "Prefiro evitar":
        itens = acessorios_por_estilo[estilo]
        acessorios_texto = "Aposte em acessórios como: " + ", ".join(itens)

    return descricao + "\n\n✨ Look sugerido: " + look_final + "\n\n🎀 " + acessorios_texto

# BOTÃO DE RESULTADO CORRIGIDO
if st.button("🔮 Me dá meu look!"):
    resposta = gerar_look_com_ia(
        ocasião, estilo, clima, humor, tempo_fora, locomocao, calçado, vibe_cor, acessorios
    )
    st.markdown("## ✅ Seu look ideal:")
    st.write(resposta)
    st.image(paletas[clima], caption=f"Paleta para clima {clima}", use_column_width=True)
