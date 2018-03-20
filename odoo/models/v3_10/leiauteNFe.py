# -*- coding: utf-8 -*-

#
# Generated Tue Mar 20 01:42:58 2018 by generateDS.py(Akretion's branch).
# Python 3.5.2 (default, Sep 14 2017, 22:51:06)  [GCC 5.4.0 20160609]
#
from odoo import fields
from .. import spec_models

# (u"Código de Regime Tributário."
# u"Este campo será obrigatoriamente preenchido com:")
CRTType = [
    ("1", u"1 – Simples Nacional"),
    ("2", u"2 – Simples Nacional – excesso de sublimite de receita bruta"),
    ("3", u"3 – Regime Normal."),
]

CSOSNType = [
    ("101", (u"101- Tributada pelo Simples Nacional com permissão de crédito."
             u"(v.2.0)")),
]

CSOSNType32 = [
    ("102", u"102- Tributada pelo Simples Nacional sem permissão de crédito."),
    ("103", (u"103 – Isenção do ICMS  no Simples Nacional para faixa de"
             u"receita bruta.")),
    ("300", u"300 – Imune."),
    ("400", u"400 – Não tributda pelo Simples Nacional (v.2.0) (v.2.0)"),
]

CSOSNType33 = [
    ("201", (u"201- Tributada pelo Simples Nacional com permissão de crédito"
             u"e com cobrança do ICMS por Substituição Tributária (v.2.0)")),
]

CSOSNType35 = [
    ("202", (u"202- Tributada pelo Simples Nacional sem permissão de crédito"
             u"e com cobrança do ICMS por Substituição Tributária")),
    ("203", (u"203-  Isenção do ICMS nos Simples Nacional para faixa de"
             u"receita bruta e com cobrança do ICMS por Substituição"
             u"Tributária (v.2.0)")),
]

# (u"500 – ICMS cobrado anterirmente por substituição tributária (substituído)"
# u"ou por antecipação"
# u"(v.2.0)")
CSOSNType37 = [
    ("500", u"500"),
]

# u"Tributação pelo ICMS 900 - Outros(v2.0)"
CSOSNType38 = [
    ("900", u"900"),
]

# u"Tributção pelo ICMS"
CSTType = [
    ("00", u"00 - Tributada integralmente"),
]

# u"Tributção pelo ICMS"
CSTType10 = [
    ("20", u"20 - Com redução de base de cálculo"),
]

# u"Tributção pelo ICMS"
CSTType12 = [
    ("30", (u"30 - Isenta ou não tributada e com cobrança do ICMS por"
            u"substituição tributária")),
]

# (u"Tributação pelo ICMS"
# u"40 - Isenta"
# u"41 - Não tributada"
# u"50 - Suspensão"
# u"51 - Diferimento")
CSTType15 = [
    ("40", u"40"),
    ("41", u"41"),
    ("50", u"50"),
]

# (u"Tributção pelo ICMS"
# u"20 - Com redução de base de cálculo")
CSTType17 = [
    ("51", u"51"),
]

# u"Tributação pelo ICMS"
CSTType19 = [
    ("60", u"60 - ICMS cobrado anteriormente por substituição tributária"),
]

# u"Tributção pelo ICMS"
CSTType20 = [
    ("70", (u"70 - Com redução de base de cálculo e cobrança do ICMS por"
            u"substituição tributária")),
]

# u"Tributção pelo ICMS"
CSTType24 = [
    ("90", u"90 - Outras"),
]

# u"Tributação pelo ICMS"
CSTType28 = [
    ("10", (u"10 - Tributada e com cobrança do ICMS por substituição"
            u"tributária")),
    ("90", u"90 – Outros."),
]

# u"Tributção pelo ICMS"
CSTType31 = [
    ("41", u"41-Não Tributado"),
]

# u"Código de Situação Tributária do PIS."
CSTType41 = [
    ("01", (u"01 – Operação Tributável - Base de Cálculo = Valor da Operação"
            u"Alíquota Normal (Cumulativo/Não Cumulativo)")),
    ("02", (u"02 - Operação Tributável - Base de Calculo = Valor da Operação"
            u"(Alíquota Diferenciada)")),
]

# u"Código de Situação Tributária do PIS."
CSTType42 = [
    ("03", (u"03 - Operação Tributável - Base de Calculo = Quantidade Vendida"
            u"x Alíquota por Unidade de Produto")),
]

# u"Código de Situação Tributária do PIS."
CSTType43 = [
    ("04", (u"04 - Operação Tributável - Tributação Monofásica - (Alíquota"
            u"Zero)")),
    ("05", u"05 - Operação Tributável (ST)"),
    ("06", u"06 - Operação Tributável - Alíquota Zero"),
    ("07", u"07 - Operação Isenta da contribuição"),
    ("08", u"08 - Operação Sem Incidência da contribuição"),
    ("09", u"09 - Operação com suspensão da contribuição"),
]

# (u"Código de Situação Tributária do PIS."
# u"99 - Outras Operações.")
CSTType44 = [
    ("49", u"49"),
    ("50", u"50"),
    ("51", u"51"),
    ("52", u"52"),
    ("53", u"53"),
    ("54", u"54"),
    ("55", u"55"),
    ("56", u"56"),
    ("60", u"60"),
    ("61", u"61"),
    ("62", u"62"),
    ("63", u"63"),
    ("64", u"64"),
    ("65", u"65"),
    ("66", u"66"),
    ("67", u"67"),
    ("70", u"70"),
    ("71", u"71"),
    ("72", u"72"),
    ("73", u"73"),
    ("74", u"74"),
    ("75", u"75"),
    ("98", u"98"),
    ("99", u"99"),
]

# u"Código de Situação Tributária do COFINS."
CSTType45 = [
    ("01", (u"01 – Operação Tributável - Base de Cálculo = Valor da Operação"
            u"Alíquota Normal (Cumulativo/Não Cumulativo)")),
    ("02", (u"02 - Operação Tributável - Base de Calculo = Valor da Operação"
            u"(Alíquota Diferenciada)")),
]

# u"Código de Situação Tributária do COFINS."
CSTType46 = [
    ("03", (u"03 - Operação Tributável - Base de Calculo = Quantidade Vendida"
            u"x Alíquota por Unidade de Produto")),
]

# u"Código de Situação Tributária do COFINS:"
CSTType47 = [
    ("04", (u"04 - Operação Tributável - Tributação Monofásica - (Alíquota"
            u"Zero)")),
    ("05", u"05 - Operação Tributável (ST)"),
    ("06", u"06 - Operação Tributável - Alíquota Zero"),
    ("07", u"07 - Operação Isenta da contribuição"),
    ("08", u"08 - Operação Sem Incidência da contribuição"),
    ("09", u"09 - Operação com suspensão da contribuição"),
]

# u"Código de Situação Tributária do COFINS:"
CSTType48 = [
    ("49", u"49 - Outras Operações de Saída"),
    ("50", (u"50 - Operação com Direito a Crédito - Vinculada Exclusivamente"
            u"a Receita Tributada no Mercado Interno")),
    ("51", (u"51 - Operação com Direito a Crédito – Vinculada Exclusivamente"
            u"a Receita Não Tributada no Mercado Interno")),
    ("52", (u"52 - Operação com Direito a Crédito - Vinculada Exclusivamente"
            u"a Receita de Exportação")),
    ("53", (u"53 - Operação com Direito a Crédito - Vinculada a Receitas"
            u"Tributadas e Não-Tributadas no Mercado Interno")),
    ("54", (u"54 - Operação com Direito a Crédito - Vinculada a Receitas"
            u"Tributadas no Mercado Interno e de Exportação")),
    ("55", (u"55 - Operação com Direito a Crédito - Vinculada a Receitas Não-"
            u"Tributadas no Mercado Interno e de Exportação")),
    ("56", (u"56 - Operação com Direito a Crédito - Vinculada a Receitas"
            u"Tributadas e Não-Tributadas no Mercado Interno, e de"
            u"Exportação")),
    ("60", (u"60 - Crédito Presumido - Operação de Aquisição Vinculada"
            u"Exclusivamente a Receita Tributada no Mercado Interno")),
    ("61", (u"61 - Crédito Presumido - Operação de Aquisição Vinculada"
            u"Exclusivamente a Receita Não-Tributada no Mercado Interno")),
    ("62", (u"62 - Crédito Presumido - Operação de Aquisição Vinculada"
            u"Exclusivamente a Receita de Exportação")),
    ("63", (u"63 - Crédito Presumido - Operação de Aquisição Vinculada a"
            u"Receitas Tributadas e Não-Tributadas no Mercado Interno")),
    ("64", (u"64 - Crédito Presumido - Operação de Aquisição Vinculada a"
            u"Receitas Tributadas no Mercado Interno e de Exportação")),
    ("65", (u"65 - Crédito Presumido - Operação de Aquisição Vinculada a"
            u"Receitas Não-Tributadas no Mercado Interno e de Exportação")),
    ("66", (u"66 - Crédito Presumido - Operação de Aquisição Vinculada a"
            u"Receitas Tributadas e Não-Tributadas no Mercado Interno, e"
            u"de Exportação")),
    ("67", u"67 - Crédito Presumido - Outras Operações"),
    ("70", u"70 - Operação de Aquisição sem Direito a Crédito"),
    ("71", u"71 - Operação de Aquisição com Isenção"),
    ("72", u"72 - Operação de Aquisição com Suspensão"),
    ("73", u"73 - Operação de Aquisição a Alíquota Zero"),
    ("74", u"74 - Operação de Aquisição sem Incidência da Contribuição"),
    ("75", u"75 - Operação de Aquisição por Substituição Tributária"),
    ("98", u"98 - Outras Operações de Entrada"),
    ("99", u"99 - Outras Operações."),
]

# u"Código da Situação Tributária do IPI:"
CSTType70 = [
    ("00", u"00-Entrada com recuperação de crédito"),
    ("49", u"49 - Outras entradas"),
    ("50", u"50-Saída tributada"),
    ("99", u"99-Outras saídas"),
]

# u"Código da Situação Tributária do IPI:"
CSTType71 = [
    ("01", u"01-Entrada tributada com alíquota zero"),
    ("02", u"02-Entrada isenta"),
    ("03", u"03-Entrada não-tributada"),
    ("04", u"04-Entrada imune"),
    ("05", u"05-Entrada com suspensão"),
    ("51", u"51-Saída tributada com alíquota zero"),
    ("52", u"52-Saída isenta"),
    ("53", u"53-Saída não-tributada"),
    ("54", u"54-Saída imune"),
    ("55", u"55-Saída com suspensão"),
]

CSTType8 = [
    ("10", (u"10 - Tributada e com cobrança do ICMS por substituição"
            u"tributária")),
]

# u"Tipo Ambiente"
TAmb = [
    ("1", u"1"),
    ("2", u"2"),
]

# u"Tipo Código da Lista de Serviços LC 116/2003"
TCListServ = [
    ("01.01", u"01.01"),
    ("01.02", u"01.02"),
    ("01.03", u"01.03"),
    ("01.04", u"01.04"),
    ("01.05", u"01.05"),
    ("01.06", u"01.06"),
    ("01.07", u"01.07"),
    ("01.08", u"01.08"),
    ("02.01", u"02.01"),
    ("03.02", u"03.02"),
    ("03.03", u"03.03"),
    ("03.04", u"03.04"),
    ("03.05", u"03.05"),
    ("04.01", u"04.01"),
    ("04.02", u"04.02"),
    ("04.03", u"04.03"),
    ("04.04", u"04.04"),
    ("04.05", u"04.05"),
    ("04.06", u"04.06"),
    ("04.07", u"04.07"),
    ("04.08", u"04.08"),
    ("04.09", u"04.09"),
    ("04.10", u"04.10"),
    ("04.11", u"04.11"),
    ("04.12", u"04.12"),
    ("04.13", u"04.13"),
    ("04.14", u"04.14"),
    ("04.15", u"04.15"),
    ("04.16", u"04.16"),
    ("04.17", u"04.17"),
    ("04.18", u"04.18"),
    ("04.19", u"04.19"),
    ("04.20", u"04.20"),
    ("04.21", u"04.21"),
    ("04.22", u"04.22"),
    ("04.23", u"04.23"),
    ("05.01", u"05.01"),
    ("05.02", u"05.02"),
    ("05.03", u"05.03"),
    ("05.04", u"05.04"),
    ("05.05", u"05.05"),
    ("05.06", u"05.06"),
    ("05.07", u"05.07"),
    ("05.08", u"05.08"),
    ("05.09", u"05.09"),
    ("06.01", u"06.01"),
    ("06.02", u"06.02"),
    ("06.03", u"06.03"),
    ("06.04", u"06.04"),
    ("06.05", u"06.05"),
    ("07.01", u"07.01"),
    ("07.02", u"07.02"),
    ("07.03", u"07.03"),
    ("07.04", u"07.04"),
    ("07.05", u"07.05"),
    ("07.06", u"07.06"),
    ("07.07", u"07.07"),
    ("07.08", u"07.08"),
    ("07.09", u"07.09"),
    ("07.10", u"07.10"),
    ("07.11", u"07.11"),
    ("07.12", u"07.12"),
    ("07.13", u"07.13"),
    ("07.16", u"07.16"),
    ("07.17", u"07.17"),
    ("07.18", u"07.18"),
    ("07.19", u"07.19"),
    ("07.20", u"07.20"),
    ("07.21", u"07.21"),
    ("07.22", u"07.22"),
    ("08.01", u"08.01"),
    ("08.02", u"08.02"),
    ("09.01", u"09.01"),
    ("09.02", u"09.02"),
    ("09.03", u"09.03"),
    ("10.01", u"10.01"),
    ("10.02", u"10.02"),
    ("10.03", u"10.03"),
    ("10.04", u"10.04"),
    ("10.05", u"10.05"),
    ("10.06", u"10.06"),
    ("10.07", u"10.07"),
    ("10.08", u"10.08"),
    ("10.09", u"10.09"),
    ("10.10", u"10.10"),
    ("11.01", u"11.01"),
    ("11.02", u"11.02"),
    ("11.03", u"11.03"),
    ("11.04", u"11.04"),
    ("12.01", u"12.01"),
    ("12.02", u"12.02"),
    ("12.03", u"12.03"),
    ("12.04", u"12.04"),
    ("12.05", u"12.05"),
    ("12.06", u"12.06"),
    ("12.07", u"12.07"),
    ("12.08", u"12.08"),
    ("12.09", u"12.09"),
    ("12.10", u"12.10"),
    ("12.11", u"12.11"),
    ("12.12", u"12.12"),
    ("12.13", u"12.13"),
    ("12.14", u"12.14"),
    ("12.15", u"12.15"),
    ("12.16", u"12.16"),
    ("12.17", u"12.17"),
    ("13.02", u"13.02"),
    ("13.03", u"13.03"),
    ("13.04", u"13.04"),
    ("13.05", u"13.05"),
    ("14.01", u"14.01"),
    ("14.02", u"14.02"),
    ("14.03", u"14.03"),
    ("14.04", u"14.04"),
    ("14.05", u"14.05"),
    ("14.06", u"14.06"),
    ("14.07", u"14.07"),
    ("14.08", u"14.08"),
    ("14.09", u"14.09"),
    ("14.10", u"14.10"),
    ("14.11", u"14.11"),
    ("14.12", u"14.12"),
    ("14.13", u"14.13"),
    ("15.01", u"15.01"),
    ("15.02", u"15.02"),
    ("15.03", u"15.03"),
    ("15.04", u"15.04"),
    ("15.05", u"15.05"),
    ("15.06", u"15.06"),
    ("15.07", u"15.07"),
    ("15.08", u"15.08"),
    ("15.09", u"15.09"),
    ("15.10", u"15.10"),
    ("15.11", u"15.11"),
    ("15.12", u"15.12"),
    ("15.13", u"15.13"),
    ("15.14", u"15.14"),
    ("15.15", u"15.15"),
    ("15.16", u"15.16"),
    ("15.17", u"15.17"),
    ("15.18", u"15.18"),
    ("16.01", u"16.01"),
    ("17.01", u"17.01"),
    ("17.02", u"17.02"),
    ("17.03", u"17.03"),
    ("17.04", u"17.04"),
    ("17.05", u"17.05"),
    ("17.06", u"17.06"),
    ("17.08", u"17.08"),
    ("17.09", u"17.09"),
    ("17.10", u"17.10"),
    ("17.11", u"17.11"),
    ("17.12", u"17.12"),
    ("17.13", u"17.13"),
    ("17.14", u"17.14"),
    ("17.15", u"17.15"),
    ("17.16", u"17.16"),
    ("17.17", u"17.17"),
    ("17.18", u"17.18"),
    ("17.19", u"17.19"),
    ("17.20", u"17.20"),
    ("17.21", u"17.21"),
    ("17.22", u"17.22"),
    ("17.23", u"17.23"),
    ("17.24", u"17.24"),
    ("18.01", u"18.01"),
    ("19.01", u"19.01"),
    ("20.01", u"20.01"),
    ("20.02", u"20.02"),
    ("20.03", u"20.03"),
    ("21.01", u"21.01"),
    ("22.01", u"22.01"),
    ("23.01", u"23.01"),
    ("24.01", u"24.01"),
    ("25.01", u"25.01"),
    ("25.02", u"25.02"),
    ("25.03", u"25.03"),
    ("25.04", u"25.04"),
    ("26.01", u"26.01"),
    ("27.01", u"27.01"),
    ("28.01", u"28.01"),
    ("29.01", u"29.01"),
    ("30.01", u"30.01"),
    ("31.01", u"31.01"),
    ("32.01", u"32.01"),
    ("33.01", u"33.01"),
    ("34.01", u"34.01"),
    ("35.01", u"35.01"),
    ("36.01", u"36.01"),
    ("37.01", u"37.01"),
    ("38.01", u"38.01"),
    ("39.01", u"39.01"),
    ("40.01", u"40.01"),
]

# u"Tipo Código de orgão (UF da tabela do IBGE + 90 RFB)"
TCOrgaoIBGE = [
    ("11", u"11"),
    ("12", u"12"),
    ("13", u"13"),
    ("14", u"14"),
    ("15", u"15"),
    ("16", u"16"),
    ("17", u"17"),
    ("21", u"21"),
    ("22", u"22"),
    ("23", u"23"),
    ("24", u"24"),
    ("25", u"25"),
    ("26", u"26"),
    ("27", u"27"),
    ("28", u"28"),
    ("29", u"29"),
    ("31", u"31"),
    ("32", u"32"),
    ("33", u"33"),
    ("35", u"35"),
    ("41", u"41"),
    ("42", u"42"),
    ("43", u"43"),
    ("50", u"50"),
    ("51", u"51"),
    ("52", u"52"),
    ("53", u"53"),
    ("90", u"90"),
    ("91", u"91"),
    ("92", u"92"),
]

# u"Tipo Código da UF da tabela do IBGE"
TCodUfIBGE = [
    ("11", u"11"),
    ("12", u"12"),
    ("13", u"13"),
    ("14", u"14"),
    ("15", u"15"),
    ("16", u"16"),
    ("17", u"17"),
    ("21", u"21"),
    ("22", u"22"),
    ("23", u"23"),
    ("24", u"24"),
    ("25", u"25"),
    ("26", u"26"),
    ("27", u"27"),
    ("28", u"28"),
    ("29", u"29"),
    ("31", u"31"),
    ("32", u"32"),
    ("33", u"33"),
    ("35", u"35"),
    ("41", u"41"),
    ("42", u"42"),
    ("43", u"43"),
    ("50", u"50"),
    ("51", u"51"),
    ("52", u"52"),
    ("53", u"53"),
]

# (u"Tipo Finalidade da NF-e (1=Normal; 2=Complementar; 3=Ajuste;"
# u"4=Devolução/Retorno)")
TFinNFe = [
    ("1", u"1"),
    ("2", u"2"),
    ("3", u"3"),
    ("4", u"4"),
]

# u"Tipo Modelo Documento Fiscal"
TMod = [
    ("55", u"55"),
    ("65", u"65"),
]

# u"Tipo processo de emissão da NF-e"
TProcEmi = [
    ("0", u"0"),
    ("1", u"1"),
    ("2", u"2"),
    ("3", u"3"),
]

# u"Tipo Sigla da UF"
TUf = [
    ("AC", u"AC"),
    ("AL", u"AL"),
    ("AM", u"AM"),
    ("AP", u"AP"),
    ("BA", u"BA"),
    ("CE", u"CE"),
    ("DF", u"DF"),
    ("ES", u"ES"),
    ("GO", u"GO"),
    ("MA", u"MA"),
    ("MG", u"MG"),
    ("MS", u"MS"),
    ("MT", u"MT"),
    ("PA", u"PA"),
    ("PB", u"PB"),
    ("PE", u"PE"),
    ("PI", u"PI"),
    ("PR", u"PR"),
    ("RJ", u"RJ"),
    ("RN", u"RN"),
    ("RO", u"RO"),
    ("RR", u"RR"),
    ("RS", u"RS"),
    ("SC", u"SC"),
    ("SE", u"SE"),
    ("SP", u"SP"),
    ("TO", u"TO"),
    ("EX", u"EX"),
]

# u"Tipo Sigla da UF de emissor // acrescentado em 24/10/08"
TUfEmi = [
    ("AC", u"AC"),
    ("AL", u"AL"),
    ("AM", u"AM"),
    ("AP", u"AP"),
    ("BA", u"BA"),
    ("CE", u"CE"),
    ("DF", u"DF"),
    ("ES", u"ES"),
    ("GO", u"GO"),
    ("MA", u"MA"),
    ("MG", u"MG"),
    ("MS", u"MS"),
    ("MT", u"MT"),
    ("PA", u"PA"),
    ("PB", u"PB"),
    ("PE", u"PE"),
    ("PI", u"PI"),
    ("PR", u"PR"),
    ("RJ", u"RJ"),
    ("RN", u"RN"),
    ("RO", u"RO"),
    ("RR", u"RR"),
    ("RS", u"RS"),
    ("SC", u"SC"),
    ("SE", u"SE"),
    ("SP", u"SP"),
    ("TO", u"TO"),
]

# u"Tipo Origem da mercadoria CST ICMS  origem da mercadoria"
Torig = [
    ("0", u"0-Nacional exceto as indicadas nos códigos 3, 4, 5 e 8"),
    ("1", u"1-Estrangeira - Importação direta"),
    ("2", u"2-Estrangeira - Adquirida no mercado interno"),
    ("3", u"3-Nacional, conteudo superior 40% e inferior ou igual a 70%"),
    ("4", u"4-Nacional, processos produtivos básicos"),
    ("5", u"5-Nacional, conteudo inferior 40%"),
    ("6", (u"6-Estrangeira - Importação direta, com similar nacional, lista"
           u"CAMEX")),
    ("7", u"7-Estrangeira - mercado interno, sem simular,lista CAMEX"),
    ("8", u"8-Nacional, Conteúdo de Importação superior a 70%."),
]

# u"Informa-se o veículo tem VIN (chassi) remarcado."
VINType = [
    ("R", u"R-Remarcado"),
    ("N", u"N-NormalVIN"),
]

# u"Código do país"
cPaisType62 = [
    ("1058", u"1058"),
]

# u"Código do regime especial de tributação"
cRegTribType = [
    ("1", u"1"),
    ("2", u"2"),
    ("3", u"3"),
    ("4", u"4"),
    ("5", u"5"),
    ("6", u"6"),
]

# u"Condição do veículo (1 - acabado; 2 - inacabado; 3 - semi-acabado)"
condVeicType = [
    ("1", u"1"),
    ("2", u"2"),
    ("3", u"3"),
]

# (u"Identificador de Local de destino da operação"
# u"(1-Interna;2-Interestadual;3-Exterior)")
idDestType = [
    ("1", u"1"),
    ("2", u"2"),
    ("3", u"3"),
]

# u"Indica operação com consumidor final (0-Não;1-Consumidor Final)"
indFinalType = [
    ("0", u"0"),
    ("1", u"1"),
]

# u"Indicador da IE do destinatário:"
indIEDestType = [
    ("1", u"1 – Contribuinte ICMSpagamento à vista"),
    ("2", u"2 – Contribuinte isento de inscrição"),
    ("9", u"9 – Não Contribuinte"),
]

# u"Exibilidade do ISS"
indISSType = [
    ("1", u"1-Exigível"),
    ("2", u"2-Não incidente"),
    ("3", u"3-Isenção"),
    ("4", u"4-Exportação"),
    ("5", u"5-Imunidade"),
    ("6", u"6-Exig.Susp. Judicial"),
    ("7", u"7-Exig.Susp. ADM"),
]

# u"Indicador de Incentivo Fiscal. 1=Sim; 2=Não"
indIncentivoType = [
    ("1", u"1"),
    ("2", u"2"),
]

# u"Indicador da forma de pagamento:"
indPagType = [
    ("0", u"0 – pagamento à vista"),
    ("1", u"1 – pagamento à prazo"),
    ("2", u"2 – outros."),
]

# (u"Indicador de presença do comprador no estabelecimento comercial no"
# u"momento da oepração"
# u"(0-Não se aplica (ex."
# u"Nota Fiscal complementar ou de ajuste"
# u"1-Operação presencial"
# u"2-Não presencial, internet"
# u"3-Não presencial, teleatendimento"
# u"4-NFC-e entrega em domicílio"
# u"9-Não presencial, outros)")
indPresType = [
    ("0", u"0"),
    ("1", u"1"),
    ("2", u"2"),
    ("3", u"3"),
    ("4", u"4"),
    ("9", u"9"),
]

# u"Origem do processo, informar com:"
indProcType = [
    ("0", u"0 - SEFAZ"),
    ("1", u"1 - Justiça Federal"),
    ("2", u"2 - Justiça Estadual"),
    ("3", u"3 - Secex/RFB"),
    ("9", u"9 - Outros"),
]

# u"Indicador de processamento síncrono. 0=NÃO; 1=SIM=Síncrono"
indSincType = [
    ("0", u"0"),
    ("1", u"1"),
]

# u"Este campo deverá ser preenchido com:"
indTotType = [
    ("0", (u"0 – o valor do item (vProd) não compõe o valor total da NF-e"
           u"(vProd)")),
    ("1", (u"1  – o valor do item (vProd) compõe o valor total da NF-e"
           u"(vProd)")),
]

# u"Modalidade de determinação da BC do ICMS ST:"
modBCSTType = [
    ("0", u"0 – Preço tabelado ou máximo  sugerido"),
    ("1", u"1 - Lista Negativa (valor)"),
    ("2", u"2 - Lista Positiva (valor)"),
    ("3", u"3 - Lista Neutra (valor)"),
    ("4", u"4 - Margem Valor Agregado (%)"),
    ("5", u"5 - Pauta (valor)"),
]

# u"Modalidade de determinação da BC do ICMS ST:"
modBCSTType13 = [
    ("0", u"0 – Preço tabelado ou máximo  sugerido"),
    ("1", u"1 - Lista Negativa (valor)"),
    ("2", u"2 - Lista Positiva (valor)"),
    ("3", u"3 - Lista Neutra (valor)"),
    ("4", u"4 - Margem Valor Agregado (%)"),
    ("5", u"5 - Pauta (valor)."),
]

# u"Modalidade de determinação da BC do ICMS ST:"
modBCSTType22 = [
    ("0", u"0 – Preço tabelado ou máximo  sugerido"),
    ("1", u"1 - Lista Negativa (valor)"),
    ("2", u"2 - Lista Positiva (valor)"),
    ("3", u"3 - Lista Neutra (valor)"),
    ("4", u"4 - Margem Valor Agregado (%)"),
    ("5", u"5 - Pauta (valor)."),
]

# u"Modalidade de determinação da BC do ICMS ST:"
modBCSTType26 = [
    ("0", u"0 – Preço tabelado ou máximo  sugerido"),
    ("1", u"1 - Lista Negativa (valor)"),
    ("2", u"2 - Lista Positiva (valor)"),
    ("3", u"3 - Lista Neutra (valor)"),
    ("4", u"4 - Margem Valor Agregado (%)"),
    ("5", u"5 - Pauta (valor)."),
]

# u"Modalidade de determinação da BC do ICMS ST:"
modBCSTType30 = [
    ("0", u"0 – Preço tabelado ou máximo  sugerido"),
    ("1", u"1 - Lista Negativa (valor)"),
    ("2", u"2 - Lista Positiva (valor)"),
    ("3", u"3 - Lista Neutra (valor)"),
    ("4", u"4 - Margem Valor Agregado (%)"),
    ("5", u"5 - Pauta (valor)."),
]

# u"Modalidade de determinação da BC do ICMS ST:"
modBCSTType34 = [
    ("0", u"0 – Preço tabelado ou máximo  sugerido"),
    ("1", u"1 - Lista Negativa (valor)"),
    ("2", u"2 - Lista Positiva (valor)"),
    ("3", u"3 - Lista Neutra (valor)"),
    ("4", u"4 - Margem Valor Agregado (%)"),
    ("5", u"5 - Pauta (valor). (v2.0)"),
]

# u"Modalidade de determinação da BC do ICMS ST:"
modBCSTType36 = [
    ("0", u"0 – Preço tabelado ou máximo  sugerido"),
    ("1", u"1 - Lista Negativa (valor)"),
    ("2", u"2 - Lista Positiva (valor)"),
    ("3", u"3 - Lista Neutra (valor)"),
    ("4", u"4 - Margem Valor Agregado (%)"),
    ("5", u"5 - Pauta (valor). (v2.0)"),
]

# u"Modalidade de determinação da BC do ICMS ST:"
modBCSTType40 = [
    ("0", u"0 – Preço tabelado ou máximo  sugerido"),
    ("1", u"1 - Lista Negativa (valor)"),
    ("2", u"2 - Lista Positiva (valor)"),
    ("3", u"3 - Lista Neutra (valor)"),
    ("4", u"4 - Margem Valor Agregado (%)"),
    ("5", u"5 - Pauta (valor)."),
]

# u"Modalidade de determinação da BC do ICMS:"
modBCType = [
    ("0", u"0 - Margem Valor Agregado (%)"),
    ("1", u"1 - Pauta (valor)"),
    ("2", u"2 - Preço Tabelado Máximo (valor)"),
    ("3", u"3 - Valor da Operação."),
]

# u"Modalidade de determinação da BC do ICMS:"
modBCType11 = [
    ("0", u"0 - Margem Valor Agregado (%)"),
    ("1", u"1 - Pauta (valor)"),
    ("2", u"2 - Preço Tabelado Máximo (valor)"),
    ("3", u"3 - Valor da Operação."),
]

# u"Modalidade de determinação da BC do ICMS:"
modBCType18 = [
    ("0", u"0 - Margem Valor Agregado (%)"),
    ("1", u"1 - Pauta (valor)"),
    ("2", u"2 - Preço Tabelado Máximo (valor)"),
    ("3", u"3 - Valor da Operação."),
]

# u"Modalidade de determinação da BC do ICMS:"
modBCType21 = [
    ("0", u"0 - Margem Valor Agregado (%)"),
    ("1", u"1 - Pauta (valor)"),
    ("2", u"2 - Preço Tabelado Máximo (valor)"),
    ("3", u"3 - Valor da Operação."),
]

# u"Modalidade de determinação da BC do ICMS:"
modBCType25 = [
    ("0", u"0 - Margem Valor Agregado (%)"),
    ("1", u"1 - Pauta (valor)"),
    ("2", u"2 - Preço Tabelado Máximo (valor)"),
    ("3", u"3 - Valor da Operação."),
]

# u"Modalidade de determinação da BC do ICMS:"
modBCType29 = [
    ("0", u"0 - Margem Valor Agregado (%)"),
    ("1", u"1 - Pauta (valor)"),
    ("2", u"2 - Preço Tabelado Máximo (valor)"),
    ("3", u"3 - Valor da Operação."),
]

# u"Modalidade de determinação da BC do ICMS:"
modBCType39 = [
    ("0", u"0 - Margem Valor Agregado (%)"),
    ("1", u"1 - Pauta (valor)"),
    ("2", u"2 - Preço Tabelado Máximo (valor)"),
    ("3", u"3 - Valor da Operação."),
]

# u"Modalidade de determinação da BC do ICMS:"
modBCType9 = [
    ("0", u"0 - Margem Valor Agregado (%)"),
    ("1", u"1 - Pauta (valor)"),
    ("2", u"2 - Preço Tabelado Máximo (valor)"),
    ("3", u"3 - Valor da Operação."),
]

# u"Modalidade do frete"
modFreteType = [
    ("0", u"0- Por conta do emitente"),
    ("1", u"1- Por conta do destinatário/remetente"),
    ("2", u"2- Por conta de terceiros"),
    ("9", u"9- Sem frete (v2.0)"),
]

# u"Código do modelo do Documento Fiscal. Utilizar 01 para NF modelo 1/1A"
modType = [
    ("01", u"01"),
]

# (u"Código do modelo do Documento Fiscal - utilizar 04 para NF de produtor"
# u"ou 01 para NF Avulsa")
modType2 = [
    ("01", u"01"),
    ("04", u"04"),
]

# (u"Código do modelo do Documento Fiscal"
# u"Preencher com '2B', quando se tratar de Cupom Fiscal emitido por máquina"
# u"registradora (não ECF), com '2C', quando se tratar de Cupom Fiscal"
# u"PDV, ou '2D', quando se tratar de Cupom Fiscal (emitido por ECF)")
modType3 = [
    ("2B", u"2B"),
    ("2C", u"2C"),
    ("2D", u"2D"),
]

# u"Motivo da desoneração do ICMS"
motDesICMSType = [
    ("3", u"3-Uso na agropecuária"),
    ("9", u"9-Outros"),
    ("12", u"12-Fomento agropecuário"),
]

# u"Motivo da desoneração do ICMS"
motDesICMSType14 = [
    ("6", u"6-Utilitários Motocicleta AÁrea Livre"),
    ("7", u"7-SUFRAMA"),
    ("9", u"9-Outros"),
]

# (u"Este campo será preenchido quando o campo anterior estiver preenchido."
# u"Informar o motivo da desoneração:")
motDesICMSType16 = [
    ("1", u"1 – Táxi"),
    ("3", u"3 – Produtor Agropecuário"),
    ("4", u"4 – Frotista/Locadora"),
    ("5", u"5 – Diplomático/Consular"),
    ("6", (u"6 – Utilitários e Motocicletas da Amazônia Ocidental e Áreas de"
           u"Livre Comércio (Resolução 714/88 e 790/94 – CONTRAN e suas"
           u"alterações)")),
    ("7", u"7 – SUFRAMA"),
    ("8", u"8 - Venda a órgão Público"),
    ("9", u"9 – Outros"),
    ("10", u"10- Deficiente Condutor"),
    ("11", u"11- Deficiente não condutor"),
    ("16", u"16 - Olimpíadas Rio 2016"),
]

# u"Motivo da desoneração do ICMS"
motDesICMSType23 = [
    ("3", u"3-Uso na agropecuária"),
    ("9", u"9-Outros"),
    ("12", u"12-Fomento agropecuário"),
]

# u"Motivo da desoneração do ICMS"
motDesICMSType27 = [
    ("3", u"3-Uso na agropecuária"),
    ("9", u"9-Outros"),
    ("12", u"12-Fomento agropecuário"),
]

# (u"Alíquota interestadual das UF envolvidas"
# u"- 4% alíquota interestadual para produtos importados"
# u"- 7% para os Estados de origem do Sul e Sudeste (exceto ES), destinado"
# u"para os Estados do Norte e Nordeste  ou ES"
# u"- 12% para os demais casos.")
pICMSInterType = [
    ("4.00", u"4.00"),
    ("7.00", u"7.00"),
    ("12.00", u"12.00"),
]

# u"Bandeira da operadora de cartão de crédito/débito"
tBandType = [
    ("01", u"01–Visa"),
    ("02", u"02–Mastercard"),
    ("03", u"03–American Express"),
    ("04", u"04–Sorocred"),
    ("99", u"99–Outros"),
]

# u"Forma de Pagamento"
tPagType = [
    ("01", u"01-Dinheiro"),
    ("02", u"02-Cheque"),
    ("03", u"03-Cartão de Crédito"),
    ("04", u"04-Cartão de Débito"),
    ("05", u"05-Crédito Loja"),
    ("10", u"10-Vale Alimentação"),
    ("11", u"11-Vale Refeição"),
    ("12", u"12-Vale Presente"),
    ("13", u"13-Vale Combustível"),
    ("99", u"99 - Outros"),
]

# u"Indicador do tipo de arma de fogo (0 - Uso permitido; 1 - Uso restrito)"
tpArmaType = [
    ("0", u"0"),
    ("1", u"1"),
]

# u"Forma de emissão da NF-e"
tpEmisType = [
    ("1", u"1 - Normal"),
    ("2", u"2 - Contingência FS"),
    ("3", u"3 - Contingência SCAN"),
    ("4", u"4 - Contingência DPEC"),
    ("5", u"5 - Contingência FSDA"),
    ("6", u"6 - Contingência SVC - AN"),
    ("7", u"7 - Contingência SVC - RS"),
    ("9", u"9 - Contingência off-line NFC-e"),
]

# (u"Formato de impressão do DANFE (0-sem DANFE;1-DANFe Retrato; 2-DANFe"
# u"Paisagem;3-DANFe Simplificado;"
# u"4-DANFe NFC-e;5-DANFe NFC-e em mensagem eletrônica)")
tpImpType = [
    ("0", u"0"),
    ("1", u"1"),
    ("2", u"2"),
    ("3", u"3"),
    ("4", u"4"),
    ("5", u"5"),
]

# (u"Tipo de Integração do processo de pagamento com o sistema de automação da"
# u"empresa/")
tpIntegraType = [
    ("1", (u"1=Pagamento integrado com o sistema de automação da empresa Ex."
           u"equipamento TEF , Comercio Eletronico")),
    ("2", (u"2=Pagamento não integrado com o sistema de automação da empresa"
           u"Ex: equipamento POS")),
]

# (u"Forma de Importação quanto a intermediação"
# u"1-por conta propria;2-por conta e ordem;3-encomenda")
tpIntermedioType = [
    ("1", u"1"),
    ("2", u"2"),
    ("3", u"3"),
]

# u"Tipo do Documento Fiscal (0 - entrada; 1 - saída)"
tpNFType = [
    ("0", u"0"),
    ("1", u"1"),
]

# (u"Tipo da Operação (1 - Venda concessionária; 2 - Faturamento direto; 3 -"
# u"Venda direta; 0 - Outros)")
tpOpType = [
    ("0", u"0"),
    ("1", u"1"),
    ("2", u"2"),
    ("3", u"3"),
]

# u"Restrição"
tpRestType = [
    ("0", u"0 - Não há"),
    ("1", u"1 - Alienação Fiduciária"),
    ("2", u"2 - Arrendamento Mercantil"),
    ("3", u"3 - Reserva de Domínio"),
    ("4", u"4 - Penhor de Veículos"),
    ("9", u"9 - outras."),
]

# (u"Via de transporte internacional informada na DI"
# u"1-Maritima;2-Fluvial;3-Lacustre;4-Aerea;5-Postal;6-Ferroviaria;7-Rodoviar"
# u"ia;8-Conduto;9-Meios Proprios;10-Entrada/Saida Ficta.")
tpViaTranspType = [
    ("1", u"1"),
    ("2", u"2"),
    ("3", u"3"),
    ("4", u"4"),
    ("5", u"5"),
    ("6", u"6"),
    ("7", u"7"),
    ("8", u"8"),
    ("9", u"9"),
    ("10", u"10"),
    ("11", u"11"),
    ("12", u"12"),
]

# u"Nome do país"
xPaisType63 = [
    ("Brasil", u"Brasil"),
    ("BRASIL", u"BRASIL"),
]


class CIDE(spec_models.AbstractSpecMixin):
    _description = u"CIDE Combustíveis"
    _name = 'nfe.v3_10.cide'
    _generateds_type = 'CIDEType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_qBCProd'

    nfe_qBCProd = fields.Monetary(
        digits=4, string="BC do CIDE", xsd_required=True,
        help=u"BC do CIDE ( Quantidade comercializada)")
    nfe_vAliqProd = fields.Monetary(
        digits=4, string="Alíquota do CIDE  (em reais)",
        xsd_required=True,
        help=u"Alíquota do CIDE  (em reais)")
    nfe_vCIDE = fields.Monetary(
        digits=2, string="Valor do CIDE", xsd_required=True,
        help=u"Valor do CIDE")


class COFINSAliq(spec_models.AbstractSpecMixin):
    _description = (u"Código de Situação Tributária do COFINS."
                    u"01 – Operação Tributável - Base de Cálculo = Valor da"
                    u"Operação"
                    u"Alíquota Normal (Cumulativo/Não Cumulativo);"
                    u"02 - Operação Tributável - Base de Calculo = Valor da"
                    u"Operação"
                    u"(Alíquota Diferenciada);")
    _name = 'nfe.v3_10.cofinsaliq'
    _generateds_type = 'COFINSAliqType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CST'

    nfe_CST = fields.Selection(
        CSTType45,
        string="Código de Situação Tributária do COFINS",
        xsd_required=True,
        help=u"Código de Situação Tributária do COFINS.")
    nfe_vBC = fields.Monetary(
        digits=2, string="Valor da BC do COFINS", xsd_required=True,
        help=u"Valor da BC do COFINS")
    nfe_pCOFINS = fields.Monetary(
        digits=2, string="Alíquota do COFINS", xsd_required=True,
        help=u"Alíquota do COFINS (em percentual)")
    nfe_vCOFINS = fields.Monetary(
        digits=2, string="Valor do COFINS", xsd_required=True,
        help=u"Valor do COFINS")


class COFINSNT(spec_models.AbstractSpecMixin):
    _description = (u"Código de Situação Tributária do COFINS:"
                    u"04 - Operação Tributável - Tributação Monofásica -"
                    u"(Alíquota Zero);"
                    u"06 - Operação Tributável - Alíquota Zero;"
                    u"07 - Operação Isenta da contribuição;"
                    u"08 - Operação Sem Incidência da contribuição;"
                    u"09 - Operação com suspensão da contribuição;")
    _name = 'nfe.v3_10.cofinsnt'
    _generateds_type = 'COFINSNTType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CST'

    nfe_CST = fields.Selection(
        CSTType47,
        string="Código de Situação Tributária do COFINS:",
        xsd_required=True,
        help=u"Código de Situação Tributária do COFINS:")


class COFINSOutr(spec_models.AbstractSpecMixin):
    _description = (u"Código de Situação Tributária do COFINS:"
                    u"49 - Outras Operações de Saída"
                    u"50 - Operação com Direito a Crédito - Vinculada"
                    u"Exclusivamente a"
                    u"Receita Tributada no Mercado Interno"
                    u"51 - Operação com Direito a Crédito – Vinculada"
                    u"Exclusivamente a"
                    u"Receita Não Tributada no Mercado Interno"
                    u"52 - Operação com Direito a Crédito - Vinculada"
                    u"Exclusivamente a"
                    u"Receita de Exportação"
                    u"53 - Operação com Direito a Crédito - Vinculada a"
                    u"Receitas Tributadas e"
                    u"Não-Tributadas no Mercado Interno"
                    u"54 - Operação com Direito a Crédito - Vinculada a"
                    u"Receitas Tributadas"
                    u"no Mercado Interno e de Exportação"
                    u"55 - Operação com Direito a Crédito - Vinculada a"
                    u"Receitas Não-"
                    u"Tributadas no Mercado Interno e de Exportação"
                    u"56 - Operação com Direito a Crédito - Vinculada a"
                    u"Receitas Tributadas e"
                    u"Não-Tributadas no Mercado Interno, e de Exportação"
                    u"60 - Crédito Presumido - Operação de Aquisição"
                    u"Vinculada Exclusivamente"
                    u"a Receita Tributada no Mercado Interno"
                    u"61 - Crédito Presumido - Operação de Aquisição"
                    u"Vinculada Exclusivamente"
                    u"a Receita Não-Tributada no Mercado Interno"
                    u"62 - Crédito Presumido - Operação de Aquisição"
                    u"Vinculada Exclusivamente"
                    u"a Receita de Exportação"
                    u"63 - Crédito Presumido - Operação de Aquisição"
                    u"Vinculada a Receitas"
                    u"Tributadas e Não-Tributadas no Mercado Interno"
                    u"64 - Crédito Presumido - Operação de Aquisição"
                    u"Vinculada a Receitas"
                    u"Tributadas no Mercado Interno e de Exportação"
                    u"65 - Crédito Presumido - Operação de Aquisição"
                    u"Vinculada a Receitas"
                    u"Não-Tributadas no Mercado Interno e de Exportação"
                    u"66 - Crédito Presumido - Operação de Aquisição"
                    u"Vinculada a Receitas"
                    u"Tributadas e Não-Tributadas no Mercado Interno, e de"
                    u"Exportação"
                    u"67 - Crédito Presumido - Outras Operações"
                    u"70 - Operação de Aquisição sem Direito a Crédito"
                    u"71 - Operação de Aquisição com Isenção"
                    u"72 - Operação de Aquisição com Suspensão"
                    u"73 - Operação de Aquisição a Alíquota Zero"
                    u"74 - Operação de Aquisição sem Incidência da"
                    u"Contribuição"
                    u"75 - Operação de Aquisição por Substituição Tributária"
                    u"98 - Outras Operações de Entrada"
                    u"99 - Outras Operações.")
    _name = 'nfe.v3_10.cofinsoutr'
    _generateds_type = 'COFINSOutrType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CST'

    nfe_choice16 = fields.Selection([
        ('nfe_vBC', 'vBC'),
        ('nfe_pCOFINS', 'pCOFINS'),
        ('nfe_qBCProd', 'qBCProd'),
        ('nfe_vAliqProd', 'vAliqProd')],
        "vBC/pCOFINS/qBCProd/vAliqProd",
        default="nfe_vBC")
    nfe_CST = fields.Selection(
        CSTType48,
        string="Código de Situação Tributária do COFINS:",
        xsd_required=True,
        help=u"Código de Situação Tributária do COFINS:")
    nfe_vBC = fields.Monetary(
        digits=2, choice='16',
        string="Valor da BC do COFINS", xsd_required=True,
        help=u"Valor da BC do COFINS")
    nfe_pCOFINS = fields.Monetary(
        digits=2, choice='16',
        string="Alíquota do COFINS", xsd_required=True,
        help=u"Alíquota do COFINS (em percentual)")
    nfe_qBCProd = fields.Monetary(
        digits=4, choice='16',
        string="Quantidade Vendida (NT2011/004) ",
        xsd_required=True,
        help=u"Quantidade Vendida (NT2011/004)")
    nfe_vAliqProd = fields.Monetary(
        digits=4, choice='16',
        string="Alíquota do COFINS",
        xsd_required=True,
        help=u"Alíquota do COFINS (em reais) (NT2011/004)")
    nfe_vCOFINS = fields.Monetary(
        digits=2, string="Valor do COFINS", xsd_required=True,
        help=u"Valor do COFINS")


class COFINSQtde(spec_models.AbstractSpecMixin):
    _description = (u"Código de Situação Tributária do COFINS."
                    u"03 - Operação Tributável - Base de Calculo ="
                    u"Quantidade Vendida x"
                    u"Alíquota por Unidade de Produto;")
    _name = 'nfe.v3_10.cofinsqtde'
    _generateds_type = 'COFINSQtdeType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CST'

    nfe_CST = fields.Selection(
        CSTType46,
        string="Código de Situação Tributária do COFINS",
        xsd_required=True,
        help=u"Código de Situação Tributária do COFINS.")
    nfe_qBCProd = fields.Monetary(
        digits=4, string="Quantidade Vendida (NT2011/004)",
        xsd_required=True,
        help=u"Quantidade Vendida (NT2011/004)")
    nfe_vAliqProd = fields.Monetary(
        digits=4, string="Alíquota do COFINS",
        xsd_required=True,
        help=u"Alíquota do COFINS (em reais) (NT2011/004)")
    nfe_vCOFINS = fields.Monetary(
        digits=2, string="Valor do COFINS", xsd_required=True,
        help=u"Valor do COFINS")


class COFINSST(spec_models.AbstractSpecMixin):
    _description = (u"Dados do COFINS da"
                    u"Substituição Tributaria;")
    _name = 'nfe.v3_10.cofinsst'
    _generateds_type = 'COFINSSTType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_vBC'

    nfe_choice17 = fields.Selection([
        ('nfe_vBC', 'vBC'),
        ('nfe_pCOFINS', 'pCOFINS'),
        ('nfe_qBCProd', 'qBCProd'),
        ('nfe_vAliqProd', 'vAliqProd')],
        "vBC/pCOFINS/qBCProd/vAliqProd",
        default="nfe_vBC")
    nfe_vBC = fields.Monetary(
        digits=2, choice='17',
        string="Valor da BC do COFINS ST",
        xsd_required=True,
        help=u"Valor da BC do COFINS ST")
    nfe_pCOFINS = fields.Monetary(
        digits=2, choice='17',
        string="Alíquota do COFINS ST",
        xsd_required=True,
        help=u"Alíquota do COFINS ST(em percentual)")
    nfe_qBCProd = fields.Monetary(
        digits=4, choice='17',
        string="Quantidade Vendida ", xsd_required=True,
        help=u"Quantidade Vendida")
    nfe_vAliqProd = fields.Monetary(
        digits=4, choice='17',
        string="Alíquota do COFINS ST(em reais)",
        xsd_required=True,
        help=u"Alíquota do COFINS ST(em reais)")
    nfe_vCOFINS = fields.Monetary(
        digits=2, string="Valor do COFINS ST", xsd_required=True,
        help=u"Valor do COFINS ST")


class COFINS(spec_models.AbstractSpecMixin):
    _description = u"Dados do COFINS"
    _name = 'nfe.v3_10.cofins'
    _generateds_type = 'COFINSType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_COFINSAliq'

    nfe_choice15 = fields.Selection([
        ('nfe_COFINSAliq', 'COFINSAliq'),
        ('nfe_COFINSQtde', 'COFINSQtde'),
        ('nfe_COFINSNT', 'COFINSNT'),
        ('nfe_COFINSOutr', 'COFINSOutr')],
        "COFINSAliq/COFINSQtde/COFINSNT/COFINSOutr",
        default="nfe_COFINSAliq")
    nfe_COFINSAliq = fields.Many2one(
        "nfe.v3_10.cofinsaliq",
        choice='15',
        string="Código de Situação Tributária do COFINS",
        xsd_required=True,
        help=(u"Código de Situação Tributária do COFINS."
              u"01 – Operação Tributável - Base de Cálculo = Valor da Operação"
              u"Alíquota Normal (Cumulativo/Não Cumulativo);"
              u"02 - Operação Tributável - Base de Calculo = Valor da Operação"
              u"(Alíquota Diferenciada);"))
    nfe_COFINSQtde = fields.Many2one(
        "nfe.v3_10.cofinsqtde",
        choice='15',
        string="Código de Situação Tributária do COFINS",
        xsd_required=True,
        help=(u"Código de Situação Tributária do COFINS."
              u"03 - Operação Tributável - Base de Calculo = Quantidade Vendida"
              u"x Alíquota por Unidade de Produto;"))
    nfe_COFINSNT = fields.Many2one(
        "nfe.v3_10.cofinsnt",
        choice='15',
        string="Código de Situação Tributária do COFINS:",
        xsd_required=True,
        help=(u"Código de Situação Tributária do COFINS:"
              u"04 - Operação Tributável - Tributação Monofásica - (Alíquota"
              u"Zero);"
              u"06 - Operação Tributável - Alíquota Zero;"
              u"07 - Operação Isenta da contribuição;"
              u"08 - Operação Sem Incidência da contribuição;"
              u"09 - Operação com suspensão da contribuição;"))
    nfe_COFINSOutr = fields.Many2one(
        "nfe.v3_10.cofinsoutr",
        choice='15',
        string="Código de Situação Tributária do COFINS:",
        xsd_required=True,
        help=(u"Código de Situação Tributária do COFINS:"
              u"49 - Outras Operações de Saída"
              u"50 - Operação com Direito a Crédito - Vinculada Exclusivamente"
              u"a Receita Tributada no Mercado Interno"
              u"51 - Operação com Direito a Crédito – Vinculada Exclusivamente"
              u"a Receita Não Tributada no Mercado Interno"
              u"52 - Operação com Direito a Crédito - Vinculada Exclusivamente"
              u"a Receita de Exportação"
              u"53 - Operação com Direito a Crédito - Vinculada a Receitas"
              u"Tributadas e Não-Tributadas no Mercado Interno"
              u"54 - Operação com Direito a Crédito - Vinculada a Receitas"
              u"Tributadas no Mercado Interno e de Exportação"
              u"55 - Operação com Direito a Crédito - Vinculada a Receitas Não-"
              u"Tributadas no Mercado Interno e de Exportação"
              u"56 - Operação com Direito a Crédito - Vinculada a Receitas"
              u"Tributadas e Não-Tributadas no Mercado Interno, e de"
              u"Exportação"
              u"60 - Crédito Presumido - Operação de Aquisição Vinculada"
              u"Exclusivamente a Receita Tributada no Mercado Interno"
              u"61 - Crédito Presumido - Operação de Aquisição Vinculada"
              u"Exclusivamente a Receita Não-Tributada no Mercado Interno"
              u"62 - Crédito Presumido - Operação de Aquisição Vinculada"
              u"Exclusivamente a Receita de Exportação"
              u"63 - Crédito Presumido - Operação de Aquisição Vinculada a"
              u"Receitas Tributadas e Não-Tributadas no Mercado Interno"
              u"64 - Crédito Presumido - Operação de Aquisição Vinculada a"
              u"Receitas Tributadas no Mercado Interno e de Exportação"
              u"65 - Crédito Presumido - Operação de Aquisição Vinculada a"
              u"Receitas Não-Tributadas no Mercado Interno e de Exportação"
              u"66 - Crédito Presumido - Operação de Aquisição Vinculada a"
              u"Receitas Tributadas e Não-Tributadas no Mercado Interno, e"
              u"de Exportação"
              u"67 - Crédito Presumido - Outras Operações"
              u"70 - Operação de Aquisição sem Direito a Crédito"
              u"71 - Operação de Aquisição com Isenção"
              u"72 - Operação de Aquisição com Suspensão"
              u"73 - Operação de Aquisição a Alíquota Zero"
              u"74 - Operação de Aquisição sem Incidência da Contribuição"
              u"75 - Operação de Aquisição por Substituição Tributária"
              u"98 - Outras Operações de Entrada"
              u"99 - Outras Operações."))


class DI(spec_models.AbstractSpecMixin):
    _description = (u"Delcaração de Importação"
                    u"(NT 2011/004)")
    _name = 'nfe.v3_10.di'
    _generateds_type = 'DIType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_nDI'

    nfe_DI_prod_id = fields.Many2one(
        "nfe.v3_10.prod")
    nfe_nDI = fields.Char(
        string="Numero do Documento de Importação DI/DSI/DA/DRI",
        xsd_required=True,
        help=(u"Numero do Documento de Importação DI/DSI/DA/DRI-E"
              u"(DI/DSI/DA/DRI-E) (NT2011/004)"))
    nfe_dDI = fields.Char(
        string="Data de registro da DI/DSI/DA",
        xsd_required=True,
        help=u"Data de registro da DI/DSI/DA (AAAA-MM-DD)")
    nfe_xLocDesemb = fields.Char(
        string="Local do desembaraço aduaneiro",
        xsd_required=True,
        help=u"Local do desembaraço aduaneiro")
    nfe_UFDesemb = fields.Selection(
        TUfEmi,
        string="UF onde ocorreu o desembaraço aduaneiro",
        xsd_required=True,
        help=u"Tipo Sigla da UF de emissor // acrescentado em 24/10/08")
    nfe_dDesemb = fields.Char(
        string="Data do desembaraço aduaneiro",
        xsd_required=True,
        help=u"Data do desembaraço aduaneiro (AAAA-MM-DD)")
    nfe_tpViaTransp = fields.Selection(
        tpViaTranspType,
        string="Via de transporte internacional informada na DI",
        xsd_required=True,
        help=(u"Via de transporte internacional informada na DI"
              u"1-Maritima;2-Fluvial;3-Lacustre;4-Aerea;5-Postal;6-Ferroviaria;"
              u"7-Rodoviaria;8-Conduto;9-Meios Proprios;10-Entrada/Saida"
              u"Ficta."))
    nfe_vAFRMM = fields.Monetary(
        digits=2, 
        string="Valor Adicional ao frete para renovação de marinha mercante",
        help=u"Valor Adicional ao frete para renovação de marinha mercante")
    nfe_tpIntermedio = fields.Selection(
        tpIntermedioType,
        string="Forma de Importação quanto a intermediação",
        xsd_required=True,
        help=(u"Forma de Importação quanto a intermediação"
              u"1-por conta propria;2-por conta e ordem;3-encomenda"))
    nfe_CNPJ = fields.Char(
        string="CNPJ do adquirente ou do encomendante",
        help=u"CNPJ do adquirente ou do encomendante")
    nfe_UFTerceiro = fields.Selection(
        TUfEmi,
        string="Sigla da UF do adquirente ou do encomendante",
        help=u"Tipo Sigla da UF de emissor // acrescentado em 24/10/08")
    nfe_cExportador = fields.Char(
        string="Código do exportador",
        xsd_required=True,
        help=(u"Código do exportador (usado nos sistemas internos de informação"
              u"do emitente da NF-e)"))
    nfe_adi = fields.One2many(
        "nfe.v3_10.adi",
        "nfe_adi_DI_id",
        string="Adições (NT 2011/004)", xsd_required=True,
        help=u"Adições (NT 2011/004)"
    )


class ICMS00(spec_models.AbstractSpecMixin):
    _description = (u"Tributação pelo ICMS"
                    u"00 - Tributada integralmente")
    _name = 'nfe.v3_10.icms00'
    _generateds_type = 'ICMS00Type'
    _concrete_class = None
    _concrete_rec_name = 'nfe_orig'

    nfe_orig = fields.Selection(
        Torig,
        string="origem da mercadoria: 0",
        xsd_required=True,
        help=u"Tipo Origem da mercadoria CST ICMS  origem da mercadoria")
    nfe_CST = fields.Selection(
        CSTType,
        string="Tributção pelo ICMS", xsd_required=True,
        help=u"Tributção pelo ICMS")
    nfe_modBC = fields.Selection(
        modBCType,
        string="Modalidade de determinação da BC do ICMS:",
        xsd_required=True,
        help=u"Modalidade de determinação da BC do ICMS:")
    nfe_vBC = fields.Monetary(
        digits=2, string="Valor da BC do ICMS", xsd_required=True,
        help=u"Valor da BC do ICMS")
    nfe_pICMS = fields.Monetary(
        digits=2, string="Alíquota do ICMS", xsd_required=True,
        help=u"Alíquota do ICMS")
    nfe_vICMS = fields.Monetary(
        digits=2, string="Valor do ICMS", xsd_required=True,
        help=u"Valor do ICMS")


class ICMS10(spec_models.AbstractSpecMixin):
    _description = (u"Tributação pelo ICMS"
                    u"10 - Tributada e com cobrança do ICMS por substituição"
                    u"tributária")
    _name = 'nfe.v3_10.icms10'
    _generateds_type = 'ICMS10Type'
    _concrete_class = None
    _concrete_rec_name = 'nfe_orig'

    nfe_orig = fields.Selection(
        Torig,
        string="origem da mercadoria: 0",
        xsd_required=True,
        help=u"Tipo Origem da mercadoria CST ICMS  origem da mercadoria")
    nfe_CST = fields.Selection(
        CSTType8,
        string="10", xsd_required=True,
        help=(u"10 - Tributada e com cobrança do ICMS por substituição"
              u"tributária"))
    nfe_modBC = fields.Selection(
        modBCType9,
        string="Modalidade de determinação da BC do ICMS:",
        xsd_required=True,
        help=u"Modalidade de determinação da BC do ICMS:")
    nfe_vBC = fields.Monetary(
        digits=2, string="Valor da BC do ICMS", xsd_required=True,
        help=u"Valor da BC do ICMS")
    nfe_pICMS = fields.Monetary(
        digits=2, string="Alíquota do ICMS", xsd_required=True,
        help=u"Alíquota do ICMS")
    nfe_vICMS = fields.Monetary(
        digits=2, string="Valor do ICMS", xsd_required=True,
        help=u"Valor do ICMS")
    nfe_modBCST = fields.Selection(
        modBCSTType,
        string="Modalidade de determinação da BC do ICMS ST:",
        xsd_required=True,
        help=u"Modalidade de determinação da BC do ICMS ST:")
    nfe_pMVAST = fields.Monetary(
        digits=2, string="Percentual da Margem de Valor Adicionado ICMS ST",
        help=u"Percentual da Margem de Valor Adicionado ICMS ST")
    nfe_pRedBCST = fields.Monetary(
        digits=2, string="Percentual de redução da BC ICMS ST",
        help=u"Percentual de redução da BC ICMS ST")
    nfe_vBCST = fields.Monetary(
        digits=2, string="Valor da BC do ICMS ST",
        xsd_required=True,
        help=u"Valor da BC do ICMS ST")
    nfe_pICMSST = fields.Monetary(
        digits=2, string="Alíquota do ICMS ST", xsd_required=True,
        help=u"Alíquota do ICMS ST")
    nfe_vICMSST = fields.Monetary(
        digits=2, string="Valor do ICMS ST", xsd_required=True,
        help=u"Valor do ICMS ST")


class ICMS20(spec_models.AbstractSpecMixin):
    _description = (u"Tributção pelo ICMS"
                    u"20 - Com redução de base de cálculo")
    _name = 'nfe.v3_10.icms20'
    _generateds_type = 'ICMS20Type'
    _concrete_class = None
    _concrete_rec_name = 'nfe_orig'

    nfe_orig = fields.Selection(
        Torig,
        string="origem da mercadoria: 0",
        xsd_required=True,
        help=u"Tipo Origem da mercadoria CST ICMS  origem da mercadoria")
    nfe_CST = fields.Selection(
        CSTType10,
        string="Tributção pelo ICMS", xsd_required=True,
        help=u"Tributção pelo ICMS")
    nfe_modBC = fields.Selection(
        modBCType11,
        string="Modalidade de determinação da BC do ICMS:",
        xsd_required=True,
        help=u"Modalidade de determinação da BC do ICMS:")
    nfe_pRedBC = fields.Monetary(
        digits=2, string="Percentual de redução da BC",
        xsd_required=True,
        help=u"Percentual de redução da BC")
    nfe_vBC = fields.Monetary(
        digits=2, string="Valor da BC do ICMS", xsd_required=True,
        help=u"Valor da BC do ICMS")
    nfe_pICMS = fields.Monetary(
        digits=2, string="Alíquota do ICMS", xsd_required=True,
        help=u"Alíquota do ICMS")
    nfe_vICMS = fields.Monetary(
        digits=2, string="Valor do ICMS", xsd_required=True,
        help=u"Valor do ICMS")
    nfe_vICMSDeson = fields.Monetary(
        digits=2, string="Valor do ICMS de desoneração",
        help=u"Valor do ICMS de desoneração")
    nfe_motDesICMS = fields.Selection(
        motDesICMSType,
        string="Motivo da desoneração do ICMS:3",
        help=u"Motivo da desoneração do ICMS")


class ICMS30(spec_models.AbstractSpecMixin):
    _description = (u"Tributação pelo ICMS"
                    u"30 - Isenta ou não tributada e com cobrança do ICMS"
                    u"por substituição"
                    u"tributária")
    _name = 'nfe.v3_10.icms30'
    _generateds_type = 'ICMS30Type'
    _concrete_class = None
    _concrete_rec_name = 'nfe_orig'

    nfe_orig = fields.Selection(
        Torig,
        string="origem da mercadoria: 0",
        xsd_required=True,
        help=u"Tipo Origem da mercadoria CST ICMS  origem da mercadoria")
    nfe_CST = fields.Selection(
        CSTType12,
        string="Tributção pelo ICMS", xsd_required=True,
        help=u"Tributção pelo ICMS")
    nfe_modBCST = fields.Selection(
        modBCSTType13,
        string="Modalidade de determinação da BC do ICMS ST:",
        xsd_required=True,
        help=u"Modalidade de determinação da BC do ICMS ST:")
    nfe_pMVAST = fields.Monetary(
        digits=2, string="Percentual da Margem de Valor Adicionado ICMS ST",
        help=u"Percentual da Margem de Valor Adicionado ICMS ST")
    nfe_pRedBCST = fields.Monetary(
        digits=2, string="Percentual de redução da BC ICMS ST",
        help=u"Percentual de redução da BC ICMS ST")
    nfe_vBCST = fields.Monetary(
        digits=2, string="Valor da BC do ICMS ST",
        xsd_required=True,
        help=u"Valor da BC do ICMS ST")
    nfe_pICMSST = fields.Monetary(
        digits=2, string="Alíquota do ICMS ST", xsd_required=True,
        help=u"Alíquota do ICMS ST")
    nfe_vICMSST = fields.Monetary(
        digits=2, string="Valor do ICMS ST", xsd_required=True,
        help=u"Valor do ICMS ST")
    nfe_vICMSDeson = fields.Monetary(
        digits=2, string="Valor do ICMS de desoneração",
        help=u"Valor do ICMS de desoneração")
    nfe_motDesICMS = fields.Selection(
        motDesICMSType14,
        string="Motivo da desoneração do ICMS:6",
        help=u"Motivo da desoneração do ICMS")


class ICMS40(spec_models.AbstractSpecMixin):
    _description = (u"Tributação pelo ICMS"
                    u"40 - Isenta"
                    u"41 - Não tributada"
                    u"50 - Suspensão")
    _name = 'nfe.v3_10.icms40'
    _generateds_type = 'ICMS40Type'
    _concrete_class = None
    _concrete_rec_name = 'nfe_orig'

    nfe_orig = fields.Selection(
        Torig,
        string="origem da mercadoria: 0",
        xsd_required=True,
        help=u"Tipo Origem da mercadoria CST ICMS  origem da mercadoria")
    nfe_CST = fields.Selection(
        CSTType15,
        string="Tributação pelo ICMS ", xsd_required=True,
        help=(u"Tributação pelo ICMS"
              u"40 - Isenta"
              u"41 - Não tributada"
              u"50 - Suspensão"
              u"51 - Diferimento"))
    nfe_vICMSDeson = fields.Monetary(
        digits=2, string="vICMSDeson",
        help=(u"O valor do ICMS será informado apenas nas operações com"
              u"veículos beneficiados com a desoneração condicional do"
              u"ICMS."))
    nfe_motDesICMS = fields.Selection(
        motDesICMSType16,
        string="motDesICMS",
        help=(u"Este campo será preenchido quando o campo anterior estiver"
              u"preenchido."
              u"Informar o motivo da desoneração:"))


class ICMS51(spec_models.AbstractSpecMixin):
    _description = (u"Tributção pelo ICMS"
                    u"51 - Diferimento"
                    u"A exigência do preenchimento das informações do ICMS"
                    u"diferido fica à"
                    u"critério de cada UF.")
    _name = 'nfe.v3_10.icms51'
    _generateds_type = 'ICMS51Type'
    _concrete_class = None
    _concrete_rec_name = 'nfe_orig'

    nfe_orig = fields.Selection(
        Torig,
        string="origem da mercadoria: 0",
        xsd_required=True,
        help=u"Tipo Origem da mercadoria CST ICMS  origem da mercadoria")
    nfe_CST = fields.Selection(
        CSTType17,
        string="Tributção pelo ICMS", xsd_required=True,
        help=(u"Tributção pelo ICMS"
              u"20 - Com redução de base de cálculo"))
    nfe_modBC = fields.Selection(
        modBCType18,
        string="Modalidade de determinação da BC do ICMS:",
        help=u"Modalidade de determinação da BC do ICMS:")
    nfe_pRedBC = fields.Monetary(
        digits=2, string="Percentual de redução da BC",
        help=u"Percentual de redução da BC")
    nfe_vBC = fields.Monetary(
        digits=2, string="Valor da BC do ICMS",
        help=u"Valor da BC do ICMS")
    nfe_pICMS = fields.Monetary(
        digits=2, string="Alíquota do ICMS",
        help=u"Alíquota do ICMS")
    nfe_vICMSOp = fields.Monetary(
        digits=2, string="Valor do ICMS da Operação",
        help=u"Valor do ICMS da Operação")
    nfe_pDif = fields.Monetary(
        digits=2, string="Percentual do diferemento",
        help=u"Percentual do diferemento")
    nfe_vICMSDif = fields.Monetary(
        digits=2, string="Valor do ICMS da diferido",
        help=u"Valor do ICMS da diferido")
    nfe_vICMS = fields.Monetary(
        digits=2, string="Valor do ICMS",
        help=u"Valor do ICMS")


class ICMS60(spec_models.AbstractSpecMixin):
    _description = (u"Tributação pelo ICMS"
                    u"60 - ICMS cobrado anteriormente por substituição"
                    u"tributária")
    _name = 'nfe.v3_10.icms60'
    _generateds_type = 'ICMS60Type'
    _concrete_class = None
    _concrete_rec_name = 'nfe_orig'

    nfe_orig = fields.Selection(
        Torig,
        string="origem da mercadoria: 0",
        xsd_required=True,
        help=u"Tipo Origem da mercadoria CST ICMS  origem da mercadoria")
    nfe_CST = fields.Selection(
        CSTType19,
        string="Tributação pelo ICMS ", xsd_required=True,
        help=u"Tributação pelo ICMS")
    nfe_vBCSTRet = fields.Monetary(
        digits=2, string="Valor da BC do ICMS ST retido anteriormente",
        help=u"Valor da BC do ICMS ST retido anteriormente")
    nfe_vICMSSTRet = fields.Monetary(
        digits=2, string="Valor do ICMS ST retido anteriormente",
        help=u"Valor do ICMS ST retido anteriormente")


class ICMS70(spec_models.AbstractSpecMixin):
    _description = (u"Tributação pelo ICMS"
                    u"70 - Com redução de base de cálculo e cobrança do ICMS"
                    u"por substituição"
                    u"tributária")
    _name = 'nfe.v3_10.icms70'
    _generateds_type = 'ICMS70Type'
    _concrete_class = None
    _concrete_rec_name = 'nfe_orig'

    nfe_orig = fields.Selection(
        Torig,
        string="origem da mercadoria: 0",
        xsd_required=True,
        help=u"Tipo Origem da mercadoria CST ICMS  origem da mercadoria")
    nfe_CST = fields.Selection(
        CSTType20,
        string="Tributção pelo ICMS", xsd_required=True,
        help=u"Tributção pelo ICMS")
    nfe_modBC = fields.Selection(
        modBCType21,
        string="Modalidade de determinação da BC do ICMS:",
        xsd_required=True,
        help=u"Modalidade de determinação da BC do ICMS:")
    nfe_pRedBC = fields.Monetary(
        digits=2, string="Percentual de redução da BC",
        xsd_required=True,
        help=u"Percentual de redução da BC")
    nfe_vBC = fields.Monetary(
        digits=2, string="Valor da BC do ICMS", xsd_required=True,
        help=u"Valor da BC do ICMS")
    nfe_pICMS = fields.Monetary(
        digits=2, string="Alíquota do ICMS", xsd_required=True,
        help=u"Alíquota do ICMS")
    nfe_vICMS = fields.Monetary(
        digits=2, string="Valor do ICMS", xsd_required=True,
        help=u"Valor do ICMS")
    nfe_modBCST = fields.Selection(
        modBCSTType22,
        string="Modalidade de determinação da BC do ICMS ST:",
        xsd_required=True,
        help=u"Modalidade de determinação da BC do ICMS ST:")
    nfe_pMVAST = fields.Monetary(
        digits=2, string="Percentual da Margem de Valor Adicionado ICMS ST",
        help=u"Percentual da Margem de Valor Adicionado ICMS ST")
    nfe_pRedBCST = fields.Monetary(
        digits=2, string="Percentual de redução da BC ICMS ST",
        help=u"Percentual de redução da BC ICMS ST")
    nfe_vBCST = fields.Monetary(
        digits=2, string="Valor da BC do ICMS ST",
        xsd_required=True,
        help=u"Valor da BC do ICMS ST")
    nfe_pICMSST = fields.Monetary(
        digits=2, string="Alíquota do ICMS ST", xsd_required=True,
        help=u"Alíquota do ICMS ST")
    nfe_vICMSST = fields.Monetary(
        digits=2, string="Valor do ICMS ST", xsd_required=True,
        help=u"Valor do ICMS ST")
    nfe_vICMSDeson = fields.Monetary(
        digits=2, string="Valor do ICMS de desoneração",
        help=u"Valor do ICMS de desoneração")
    nfe_motDesICMS = fields.Selection(
        motDesICMSType23,
        string="Motivo da desoneração do ICMS:3",
        help=u"Motivo da desoneração do ICMS")


class ICMS90(spec_models.AbstractSpecMixin):
    _description = (u"Tributação pelo ICMS"
                    u"90 - Outras")
    _name = 'nfe.v3_10.icms90'
    _generateds_type = 'ICMS90Type'
    _concrete_class = None
    _concrete_rec_name = 'nfe_orig'

    nfe_orig = fields.Selection(
        Torig,
        string="origem da mercadoria: 0",
        xsd_required=True,
        help=u"Tipo Origem da mercadoria CST ICMS  origem da mercadoria")
    nfe_CST = fields.Selection(
        CSTType24,
        string="Tributção pelo ICMS", xsd_required=True,
        help=u"Tributção pelo ICMS")
    nfe_modBC = fields.Selection(
        modBCType25,
        string="Modalidade de determinação da BC do ICMS:",
        help=u"Modalidade de determinação da BC do ICMS:")
    nfe_vBC = fields.Monetary(
        digits=2, string="Valor da BC do ICMS",
        help=u"Valor da BC do ICMS")
    nfe_pRedBC = fields.Monetary(
        digits=2, string="Percentual de redução da BC",
        help=u"Percentual de redução da BC")
    nfe_pICMS = fields.Monetary(
        digits=2, string="Alíquota do ICMS",
        help=u"Alíquota do ICMS")
    nfe_vICMS = fields.Monetary(
        digits=2, string="Valor do ICMS",
        help=u"Valor do ICMS")
    nfe_modBCST = fields.Selection(
        modBCSTType26,
        string="Modalidade de determinação da BC do ICMS ST:",
        help=u"Modalidade de determinação da BC do ICMS ST:")
    nfe_pMVAST = fields.Monetary(
        digits=2, string="Percentual da Margem de Valor Adicionado ICMS ST",
        help=u"Percentual da Margem de Valor Adicionado ICMS ST")
    nfe_pRedBCST = fields.Monetary(
        digits=2, string="Percentual de redução da BC ICMS ST",
        help=u"Percentual de redução da BC ICMS ST")
    nfe_vBCST = fields.Monetary(
        digits=2, string="Valor da BC do ICMS ST",
        help=u"Valor da BC do ICMS ST")
    nfe_pICMSST = fields.Monetary(
        digits=2, string="Alíquota do ICMS ST",
        help=u"Alíquota do ICMS ST")
    nfe_vICMSST = fields.Monetary(
        digits=2, string="Valor do ICMS ST",
        help=u"Valor do ICMS ST")
    nfe_vICMSDeson = fields.Monetary(
        digits=2, string="Valor do ICMS de desoneração",
        help=u"Valor do ICMS de desoneração")
    nfe_motDesICMS = fields.Selection(
        motDesICMSType27,
        string="Motivo da desoneração do ICMS:3",
        help=u"Motivo da desoneração do ICMS")


class ICMSPart(spec_models.AbstractSpecMixin):
    _description = (u"Partilha do ICMS entre a UF de origem e UF de destino ou a"
                    u"UF definida"
                    u"na legislação"
                    u"Operação interestadual para consumidor final com"
                    u"partilha do ICMS"
                    u"devido na operação entre a UF de origem e a UF do"
                    u"destinatário ou"
                    u"ou a UF definida na legislação. (Ex. UF da"
                    u"concessionária de"
                    u"entrega do  veículos)")
    _name = 'nfe.v3_10.icmspart'
    _generateds_type = 'ICMSPartType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_orig'

    nfe_orig = fields.Selection(
        Torig,
        string="origem da mercadoria: 0",
        xsd_required=True,
        help=u"Tipo Origem da mercadoria CST ICMS  origem da mercadoria")
    nfe_CST = fields.Selection(
        CSTType28,
        string="Tributação pelo ICMS ", xsd_required=True,
        help=u"Tributação pelo ICMS")
    nfe_modBC = fields.Selection(
        modBCType29,
        string="Modalidade de determinação da BC do ICMS:",
        xsd_required=True,
        help=u"Modalidade de determinação da BC do ICMS:")
    nfe_vBC = fields.Monetary(
        digits=2, string="Valor da BC do ICMS", xsd_required=True,
        help=u"Valor da BC do ICMS")
    nfe_pRedBC = fields.Monetary(
        digits=2, string="Percentual de redução da BC",
        help=u"Percentual de redução da BC")
    nfe_pICMS = fields.Monetary(
        digits=2, string="Alíquota do ICMS", xsd_required=True,
        help=u"Alíquota do ICMS")
    nfe_vICMS = fields.Monetary(
        digits=2, string="Valor do ICMS", xsd_required=True,
        help=u"Valor do ICMS")
    nfe_modBCST = fields.Selection(
        modBCSTType30,
        string="Modalidade de determinação da BC do ICMS ST:",
        xsd_required=True,
        help=u"Modalidade de determinação da BC do ICMS ST:")
    nfe_pMVAST = fields.Monetary(
        digits=2, string="Percentual da Margem de Valor Adicionado ICMS ST",
        help=u"Percentual da Margem de Valor Adicionado ICMS ST")
    nfe_pRedBCST = fields.Monetary(
        digits=2, string="Percentual de redução da BC ICMS ST",
        help=u"Percentual de redução da BC ICMS ST")
    nfe_vBCST = fields.Monetary(
        digits=2, string="Valor da BC do ICMS ST",
        xsd_required=True,
        help=u"Valor da BC do ICMS ST")
    nfe_pICMSST = fields.Monetary(
        digits=2, string="Alíquota do ICMS ST", xsd_required=True,
        help=u"Alíquota do ICMS ST")
    nfe_vICMSST = fields.Monetary(
        digits=2, string="Valor do ICMS ST", xsd_required=True,
        help=u"Valor do ICMS ST")
    nfe_pBCOp = fields.Monetary(
        digits=2, string="pBCOp", xsd_required=True,
        help=(u"Percentual para determinação do valor  da Base de Cálculo da"
              u"operação própria."))
    nfe_UFST = fields.Selection(
        TUf,
        string="Sigla da UF para qual é devido o ICMS ST da operação",
        xsd_required=True,
        help=u"Tipo Sigla da UF")


class ICMSSN101(spec_models.AbstractSpecMixin):
    _description = (u"Tributação do ICMS pelo SIMPLES NACIONAL e CSOSN=101"
                    u"(v.2.0)")
    _name = 'nfe.v3_10.icmssn101'
    _generateds_type = 'ICMSSN101Type'
    _concrete_class = None
    _concrete_rec_name = 'nfe_orig'

    nfe_orig = fields.Selection(
        Torig,
        string="origem da mercadoria: 0",
        xsd_required=True,
        help=u"Tipo Origem da mercadoria CST ICMS  origem da mercadoria")
    nfe_CSOSN = fields.Selection(
        CSOSNType,
        string="101", xsd_required=True,
        help=(u"101- Tributada pelo Simples Nacional com permissão de crédito."
              u"(v.2.0)"))
    nfe_pCredSN = fields.Monetary(
        digits=2, string="Alíquota aplicável de cálculo do crédito",
        xsd_required=True,
        help=(u"Alíquota aplicável de cálculo do crédito (Simples Nacional)."
              u"(v2.0)"))
    nfe_vCredICMSSN = fields.Monetary(
        digits=2, string="vCredICMSSN", xsd_required=True,
        help=(u"Valor crédito do ICMS que pode ser aproveitado nos termos do"
              u"art. 23 da LC 123 (Simples Nacional) (v2.0)"))


class ICMSSN102(spec_models.AbstractSpecMixin):
    _description = (u"Tributação do ICMS pelo SIMPLES NACIONAL e CSOSN=102, 103,"
                    u"300 ou 400"
                    u"(v.2.0))")
    _name = 'nfe.v3_10.icmssn102'
    _generateds_type = 'ICMSSN102Type'
    _concrete_class = None
    _concrete_rec_name = 'nfe_orig'

    nfe_orig = fields.Selection(
        Torig,
        string="origem da mercadoria: 0",
        xsd_required=True,
        help=u"Tipo Origem da mercadoria CST ICMS  origem da mercadoria")
    nfe_CSOSN = fields.Selection(
        CSOSNType32,
        string="102", xsd_required=True,
        help=(u"102- Tributada pelo Simples Nacional sem permissão de crédito."
              u"103 – Isenção do ICMS  no Simples Nacional para faixa de"
              u"receita bruta."
              u"300 – Imune."
              u"400 – Não tributda pelo Simples Nacional (v.2.0) (v.2.0)"))


class ICMSSN201(spec_models.AbstractSpecMixin):
    _description = (u"Tributação do ICMS pelo SIMPLES NACIONAL e CSOSN=201"
                    u"(v.2.0)")
    _name = 'nfe.v3_10.icmssn201'
    _generateds_type = 'ICMSSN201Type'
    _concrete_class = None
    _concrete_rec_name = 'nfe_orig'

    nfe_orig = fields.Selection(
        Torig,
        string="Origem da mercadoria:", xsd_required=True,
        help=u"Tipo Origem da mercadoria CST ICMS  origem da mercadoria")
    nfe_CSOSN = fields.Selection(
        CSOSNType33,
        string="201", xsd_required=True,
        help=(u"201- Tributada pelo Simples Nacional com permissão de crédito e"
              u"com cobrança do ICMS por Substituição Tributária (v.2.0)"))
    nfe_modBCST = fields.Selection(
        modBCSTType34,
        string="Modalidade de determinação da BC do ICMS ST:",
        xsd_required=True,
        help=u"Modalidade de determinação da BC do ICMS ST:")
    nfe_pMVAST = fields.Monetary(
        digits=2, string="Percentual da Margem de Valor Adicionado ICMS ST",
        help=u"Percentual da Margem de Valor Adicionado ICMS ST (v2.0)")
    nfe_pRedBCST = fields.Monetary(
        digits=2, string="Percentual de redução da BC ICMS ST",
        help=u"Percentual de redução da BC ICMS ST  (v2.0)")
    nfe_vBCST = fields.Monetary(
        digits=2, string="Valor da BC do ICMS ST (v2.0)",
        xsd_required=True,
        help=u"Valor da BC do ICMS ST (v2.0)")
    nfe_pICMSST = fields.Monetary(
        digits=2, string="Alíquota do ICMS ST (v2.0)",
        xsd_required=True,
        help=u"Alíquota do ICMS ST (v2.0)")
    nfe_vICMSST = fields.Monetary(
        digits=2, string="Valor do ICMS ST (v2.0)",
        xsd_required=True,
        help=u"Valor do ICMS ST (v2.0)")
    nfe_pCredSN = fields.Monetary(
        digits=2, string="Alíquota aplicável de cálculo do crédito",
        xsd_required=True,
        help=(u"Alíquota aplicável de cálculo do crédito (Simples Nacional)."
              u"(v2.0)"))
    nfe_vCredICMSSN = fields.Monetary(
        digits=2, string="vCredICMSSN", xsd_required=True,
        help=(u"Valor crédito do ICMS que pode ser aproveitado nos termos do"
              u"art. 23 da LC 123 (Simples Nacional) (v2.0)"))


class ICMSSN202(spec_models.AbstractSpecMixin):
    _description = (u"Tributação do ICMS pelo SIMPLES NACIONAL e CSOSN=202 ou"
                    u"203 (v.2.0)")
    _name = 'nfe.v3_10.icmssn202'
    _generateds_type = 'ICMSSN202Type'
    _concrete_class = None
    _concrete_rec_name = 'nfe_orig'

    nfe_orig = fields.Selection(
        Torig,
        string="Origem da mercadoria:", xsd_required=True,
        help=u"Tipo Origem da mercadoria CST ICMS  origem da mercadoria")
    nfe_CSOSN = fields.Selection(
        CSOSNType35,
        string="202", xsd_required=True,
        help=(u"202- Tributada pelo Simples Nacional sem permissão de crédito e"
              u"com cobrança do ICMS por Substituição Tributária;"
              u"203-  Isenção do ICMS nos Simples Nacional para faixa de"
              u"receita bruta e com cobrança do ICMS por Substituição"
              u"Tributária (v.2.0)"))
    nfe_modBCST = fields.Selection(
        modBCSTType36,
        string="Modalidade de determinação da BC do ICMS ST:",
        xsd_required=True,
        help=u"Modalidade de determinação da BC do ICMS ST:")
    nfe_pMVAST = fields.Monetary(
        digits=2, string="Percentual da Margem de Valor Adicionado ICMS ST",
        help=u"Percentual da Margem de Valor Adicionado ICMS ST (v2.0)")
    nfe_pRedBCST = fields.Monetary(
        digits=2, string="Percentual de redução da BC ICMS ST",
        help=u"Percentual de redução da BC ICMS ST  (v2.0)")
    nfe_vBCST = fields.Monetary(
        digits=2, string="Valor da BC do ICMS ST (v2.0)",
        xsd_required=True,
        help=u"Valor da BC do ICMS ST (v2.0)")
    nfe_pICMSST = fields.Monetary(
        digits=2, string="Alíquota do ICMS ST (v2.0)",
        xsd_required=True,
        help=u"Alíquota do ICMS ST (v2.0)")
    nfe_vICMSST = fields.Monetary(
        digits=2, string="Valor do ICMS ST (v2.0)",
        xsd_required=True,
        help=u"Valor do ICMS ST (v2.0)")


class ICMSSN500(spec_models.AbstractSpecMixin):
    _description = (u"Tributação do ICMS pelo SIMPLES NACIONAL,CRT=1 – Simples"
                    u"Nacional e"
                    u"CSOSN=500 (v.2.0)")
    _name = 'nfe.v3_10.icmssn500'
    _generateds_type = 'ICMSSN500Type'
    _concrete_class = None
    _concrete_rec_name = 'nfe_orig'

    nfe_orig = fields.Selection(
        Torig,
        string="origem da mercadoria: 0",
        xsd_required=True,
        help=u"Tipo Origem da mercadoria CST ICMS  origem da mercadoria")
    nfe_CSOSN = fields.Selection(
        CSOSNType37,
        string="500 – ICMS cobrado anterirmente por substituição tributária",
        xsd_required=True,
        help=(u"500 – ICMS cobrado anterirmente por substituição tributária"
              u"(substituído) ou por antecipação"
              u"(v.2.0)"))
    nfe_vBCSTRet = fields.Monetary(
        digits=2, string="Valor da BC do ICMS ST retido anteriormente",
        help=u"Valor da BC do ICMS ST retido anteriormente (v2.0)")
    nfe_vICMSSTRet = fields.Monetary(
        digits=2, string="Valor do ICMS ST retido anteriormente",
        help=u"Valor do ICMS ST retido anteriormente  (v2.0)")


class ICMSSN900(spec_models.AbstractSpecMixin):
    _description = (u"Tributação do ICMS pelo SIMPLES NACIONAL, CRT=1 – Simples"
                    u"Nacional e"
                    u"CSOSN=900 (v2.0)")
    _name = 'nfe.v3_10.icmssn900'
    _generateds_type = 'ICMSSN900Type'
    _concrete_class = None
    _concrete_rec_name = 'nfe_orig'

    nfe_orig = fields.Selection(
        Torig,
        string="origem da mercadoria: 0",
        xsd_required=True,
        help=u"Tipo Origem da mercadoria CST ICMS  origem da mercadoria")
    nfe_CSOSN = fields.Selection(
        CSOSNType38,
        string="Tributação pelo ICMS 900",
        xsd_required=True,
        help=u"Tributação pelo ICMS 900 - Outros(v2.0)")
    nfe_modBC = fields.Selection(
        modBCType39,
        string="Modalidade de determinação da BC do ICMS:",
        help=u"Modalidade de determinação da BC do ICMS:")
    nfe_vBC = fields.Monetary(
        digits=2, string="Valor da BC do ICMS",
        help=u"Valor da BC do ICMS")
    nfe_pRedBC = fields.Monetary(
        digits=2, string="Percentual de redução da BC",
        help=u"Percentual de redução da BC")
    nfe_pICMS = fields.Monetary(
        digits=2, string="Alíquota do ICMS",
        help=u"Alíquota do ICMS")
    nfe_vICMS = fields.Monetary(
        digits=2, string="Valor do ICMS",
        help=u"Valor do ICMS")
    nfe_modBCST = fields.Selection(
        modBCSTType40,
        string="Modalidade de determinação da BC do ICMS ST:",
        help=u"Modalidade de determinação da BC do ICMS ST:")
    nfe_pMVAST = fields.Monetary(
        digits=2, string="Percentual da Margem de Valor Adicionado ICMS ST",
        help=u"Percentual da Margem de Valor Adicionado ICMS ST")
    nfe_pRedBCST = fields.Monetary(
        digits=2, string="Percentual de redução da BC ICMS ST",
        help=u"Percentual de redução da BC ICMS ST")
    nfe_vBCST = fields.Monetary(
        digits=2, string="Valor da BC do ICMS ST",
        help=u"Valor da BC do ICMS ST")
    nfe_pICMSST = fields.Monetary(
        digits=2, string="Alíquota do ICMS ST",
        help=u"Alíquota do ICMS ST")
    nfe_vICMSST = fields.Monetary(
        digits=2, string="Valor do ICMS ST",
        help=u"Valor do ICMS ST")
    nfe_pCredSN = fields.Monetary(
        digits=2, string="Alíquota aplicável de cálculo do crédito",
        help=(u"Alíquota aplicável de cálculo do crédito (Simples Nacional)."
              u"(v2.0)"))
    nfe_vCredICMSSN = fields.Monetary(
        digits=2, string="vCredICMSSN",
        help=(u"Valor crédito do ICMS que pode ser aproveitado nos termos do"
              u"art. 23 da LC 123 (Simples Nacional) (v2.0)"))


class ICMSST(spec_models.AbstractSpecMixin):
    _description = (u"Grupo de informação do ICMSST devido para a UF de destino,"
                    u"nas"
                    u"operações interestaduais de produtos que tiveram"
                    u"retenção"
                    u"antecipada de ICMS por ST na UF do remetente. Repasse"
                    u"via"
                    u"Substituto Tributário.")
    _name = 'nfe.v3_10.icmsst'
    _generateds_type = 'ICMSSTType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_orig'

    nfe_orig = fields.Selection(
        Torig,
        string="origem da mercadoria: 0",
        xsd_required=True,
        help=u"Tipo Origem da mercadoria CST ICMS  origem da mercadoria")
    nfe_CST = fields.Selection(
        CSTType31,
        string="Tributção pelo ICMS", xsd_required=True,
        help=u"Tributção pelo ICMS")
    nfe_vBCSTRet = fields.Monetary(
        digits=2, 
        string="Informar o valor da BC do ICMS ST retido na UF remetente",
        xsd_required=True,
        help=u"Informar o valor da BC do ICMS ST retido na UF remetente")
    nfe_vICMSSTRet = fields.Monetary(
        digits=2, string="Informar o valor do ICMS ST retido na UF remetente",
        xsd_required=True,
        help=u"Informar o valor do ICMS ST retido na UF remetente (iv2.0))")
    nfe_vBCSTDest = fields.Monetary(
        digits=2, string="Informar o valor da BC do ICMS ST da UF destino",
        xsd_required=True,
        help=u"Informar o valor da BC do ICMS ST da UF destino")
    nfe_vICMSSTDest = fields.Monetary(
        digits=2, string="Informar o valor da BC do ICMS ST da UF destino",
        xsd_required=True,
        help=u"Informar o valor da BC do ICMS ST da UF destino (v2.0)")


class ICMSTot(spec_models.AbstractSpecMixin):
    _description = u"Totais referentes ao ICMS"
    _name = 'nfe.v3_10.icmstot'
    _generateds_type = 'ICMSTotType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_vBC'

    nfe_vBC = fields.Monetary(
        digits=2, string="BC do ICMS", xsd_required=True,
        help=u"BC do ICMS")
    nfe_vICMS = fields.Monetary(
        digits=2, string="Valor Total do ICMS", xsd_required=True,
        help=u"Valor Total do ICMS")
    nfe_vICMSDeson = fields.Monetary(
        digits=2, string="Valor Total do ICMS desonerado",
        xsd_required=True,
        help=u"Valor Total do ICMS desonerado")
    nfe_vFCPUFDest = fields.Monetary(
        digits=2, 
        string="Valor total do ICMS relativo ao Fundo de Combate à Pobreza",
        help=(u"Valor total do ICMS relativo ao Fundo de Combate à Pobreza"
              u"(FCP) para a UF de destino."))
    nfe_vICMSUFDest = fields.Monetary(
        digits=2, 
        string="Valor total do ICMS de partilha para a UF do destinatário",
        help=u"Valor total do ICMS de partilha para a UF do destinatário")
    nfe_vICMSUFRemet = fields.Monetary(
        digits=2, 
        string="Valor total do ICMS de partilha para a UF do remetente",
        help=u"Valor total do ICMS de partilha para a UF do remetente")
    nfe_vBCST = fields.Monetary(
        digits=2, string="BC do ICMS ST", xsd_required=True,
        help=u"BC do ICMS ST")
    nfe_vST = fields.Monetary(
        digits=2, string="Valor Total do ICMS ST", xsd_required=True,
        help=u"Valor Total do ICMS ST")
    nfe_vProd = fields.Monetary(
        digits=2, string="Valor Total dos produtos e serviços",
        xsd_required=True,
        help=u"Valor Total dos produtos e serviços")
    nfe_vFrete = fields.Monetary(
        digits=2, string="Valor Total do Frete", xsd_required=True,
        help=u"Valor Total do Frete")
    nfe_vSeg = fields.Monetary(
        digits=2, string="Valor Total do Seguro", xsd_required=True,
        help=u"Valor Total do Seguro")
    nfe_vDesc = fields.Monetary(
        digits=2, string="Valor Total do Desconto",
        xsd_required=True,
        help=u"Valor Total do Desconto")
    nfe_vII = fields.Monetary(
        digits=2, string="Valor Total do II", xsd_required=True,
        help=u"Valor Total do II")
    nfe_vIPI = fields.Monetary(
        digits=2, string="Valor Total do IPI", xsd_required=True,
        help=u"Valor Total do IPI")
    nfe_vPIS = fields.Monetary(
        digits=2, string="Valor do PIS", xsd_required=True,
        help=u"Valor do PIS")
    nfe_vCOFINS = fields.Monetary(
        digits=2, string="Valor do COFINS", xsd_required=True,
        help=u"Valor do COFINS")
    nfe_vOutro = fields.Monetary(
        digits=2, string="Outras Despesas acessórias",
        xsd_required=True,
        help=u"Outras Despesas acessórias")
    nfe_vNF = fields.Monetary(
        digits=2, string="Valor Total da NF-e", xsd_required=True,
        help=u"Valor Total da NF-e")
    nfe_vTotTrib = fields.Monetary(
        digits=2, string="Valor estimado total de impostos federais",
        help=(u"Valor estimado total de impostos federais, estaduais e"
              u"municipais"))


class ICMS(spec_models.AbstractSpecMixin):
    _description = u"Dados do ICMS Normal e ST"
    _name = 'nfe.v3_10.icms'
    _generateds_type = 'ICMSType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_ICMS00'

    nfe_choice11 = fields.Selection([
        ('nfe_ICMS00', 'ICMS00'),
        ('nfe_ICMS10', 'ICMS10'),
        ('nfe_ICMS20', 'ICMS20'),
        ('nfe_ICMS30', 'ICMS30'),
        ('nfe_ICMS40', 'ICMS40'),
        ('nfe_ICMS51', 'ICMS51'),
        ('nfe_ICMS60', 'ICMS60'),
        ('nfe_ICMS70', 'ICMS70'),
        ('nfe_ICMS90', 'ICMS90'),
        ('nfe_ICMSPart', 'ICMSPart'),
        ('nfe_ICMSST', 'ICMSST'),
        ('nfe_ICMSSN101', 'ICMSSN101'),
        ('nfe_ICMSSN102', 'ICMSSN102'),
        ('nfe_ICMSSN201', 'ICMSSN201'),
        ('nfe_ICMSSN202', 'ICMSSN202'),
        ('nfe_ICMSSN500', 'ICMSSN500'),
        ('nfe_ICMSSN900', 'ICMSSN900')],
        "ICMS00/ICMS10/ICMS20/ICMS30/ICMS40/ICMS51/ICMS60/I...",
        default="nfe_ICMS00")
    nfe_ICMS00 = fields.Many2one(
        "nfe.v3_10.icms00",
        choice='11',
        string="Tributação pelo ICMS", xsd_required=True,
        help=(u"Tributação pelo ICMS"
              u"00 - Tributada integralmente"))
    nfe_ICMS10 = fields.Many2one(
        "nfe.v3_10.icms10",
        choice='11',
        string="Tributação pelo ICMS", xsd_required=True,
        help=(u"Tributação pelo ICMS"
              u"10 - Tributada e com cobrança do ICMS por substituição"
              u"tributária"))
    nfe_ICMS20 = fields.Many2one(
        "nfe.v3_10.icms20",
        choice='11',
        string="Tributção pelo ICMS", xsd_required=True,
        help=(u"Tributção pelo ICMS"
              u"20 - Com redução de base de cálculo"))
    nfe_ICMS30 = fields.Many2one(
        "nfe.v3_10.icms30",
        choice='11',
        string="Tributação pelo ICMS", xsd_required=True,
        help=(u"Tributação pelo ICMS"
              u"30 - Isenta ou não tributada e com cobrança do ICMS por"
              u"substituição tributária"))
    nfe_ICMS40 = fields.Many2one(
        "nfe.v3_10.icms40",
        choice='11',
        string="Tributação pelo ICMS", xsd_required=True,
        help=(u"Tributação pelo ICMS"
              u"40 - Isenta"
              u"41 - Não tributada"
              u"50 - Suspensão"))
    nfe_ICMS51 = fields.Many2one(
        "nfe.v3_10.icms51",
        choice='11',
        string="Tributção pelo ICMS", xsd_required=True,
        help=(u"Tributção pelo ICMS"
              u"51 - Diferimento"
              u"A exigência do preenchimento das informações do ICMS diferido"
              u"fica à critério de cada UF."))
    nfe_ICMS60 = fields.Many2one(
        "nfe.v3_10.icms60",
        choice='11',
        string="Tributação pelo ICMS", xsd_required=True,
        help=(u"Tributação pelo ICMS"
              u"60 - ICMS cobrado anteriormente por substituição tributária"))
    nfe_ICMS70 = fields.Many2one(
        "nfe.v3_10.icms70",
        choice='11',
        string="Tributação pelo ICMS ",
        xsd_required=True,
        help=(u"Tributação pelo ICMS"
              u"70 - Com redução de base de cálculo e cobrança do ICMS por"
              u"substituição tributária"))
    nfe_ICMS90 = fields.Many2one(
        "nfe.v3_10.icms90",
        choice='11',
        string="Tributação pelo ICMS", xsd_required=True,
        help=(u"Tributação pelo ICMS"
              u"90 - Outras"))
    nfe_ICMSPart = fields.Many2one(
        "nfe.v3_10.icmspart",
        choice='11',
        string="ICMSPart", xsd_required=True,
        help=(u"Partilha do ICMS entre a UF de origem e UF de destino ou a UF"
              u"definida na legislação"
              u"Operação interestadual para consumidor final com partilha do"
              u"ICMS  devido na operação entre a UF de origem e a UF do"
              u"destinatário ou ou a UF definida na legislação. (Ex. UF da"
              u"concessionária de entrega do  veículos)"))
    nfe_ICMSST = fields.Many2one(
        "nfe.v3_10.icmsst",
        choice='11',
        string="Grupo de informação do ICMSST devido para a UF de destino",
        xsd_required=True,
        help=(u"Grupo de informação do ICMSST devido para a UF de destino, nas"
              u"operações interestaduais de produtos que tiveram retenção"
              u"antecipada de ICMS por ST na UF do remetente. Repasse via"
              u"Substituto Tributário."))
    nfe_ICMSSN101 = fields.Many2one(
        "nfe.v3_10.icmssn101",
        choice='11',
        string="Tributação do ICMS pelo SIMPLES NACIONAL e CSOSN=101",
        xsd_required=True,
        help=u"Tributação do ICMS pelo SIMPLES NACIONAL e CSOSN=101 (v.2.0)")
    nfe_ICMSSN102 = fields.Many2one(
        "nfe.v3_10.icmssn102",
        choice='11',
        string="Tributação do ICMS pelo SIMPLES NACIONAL e CSOSN=102",
        xsd_required=True,
        help=(u"Tributação do ICMS pelo SIMPLES NACIONAL e CSOSN=102, 103, 300"
              u"ou 400 (v.2.0))"))
    nfe_ICMSSN201 = fields.Many2one(
        "nfe.v3_10.icmssn201",
        choice='11',
        string="Tributação do ICMS pelo SIMPLES NACIONAL e CSOSN=201",
        xsd_required=True,
        help=u"Tributação do ICMS pelo SIMPLES NACIONAL e CSOSN=201 (v.2.0)")
    nfe_ICMSSN202 = fields.Many2one(
        "nfe.v3_10.icmssn202",
        choice='11',
        string="Tributação do ICMS pelo SIMPLES NACIONAL e CSOSN=202 ou 203",
        xsd_required=True,
        help=(u"Tributação do ICMS pelo SIMPLES NACIONAL e CSOSN=202 ou 203"
              u"(v.2.0)"))
    nfe_ICMSSN500 = fields.Many2one(
        "nfe.v3_10.icmssn500",
        choice='11',
        string="Tributação do ICMS pelo SIMPLES NACIONAL",
        xsd_required=True,
        help=(u"Tributação do ICMS pelo SIMPLES NACIONAL,CRT=1 – Simples"
              u"Nacional e CSOSN=500 (v.2.0)"))
    nfe_ICMSSN900 = fields.Many2one(
        "nfe.v3_10.icmssn900",
        choice='11',
        string="Tributação do ICMS pelo SIMPLES NACIONAL",
        xsd_required=True,
        help=(u"Tributação do ICMS pelo SIMPLES NACIONAL, CRT=1 – Simples"
              u"Nacional e CSOSN=900 (v2.0)"))


class ICMSUFDest(spec_models.AbstractSpecMixin):
    _description = (u"Grupo a ser informado nas vendas interestarduais para"
                    u"consumidor final,"
                    u"não contribuinte de ICMS")
    _name = 'nfe.v3_10.icmsufdest'
    _generateds_type = 'ICMSUFDestType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_vBCUFDest'

    nfe_vBCUFDest = fields.Monetary(
        digits=2, 
        string="Valor da Base de Cálculo do ICMS na UF do destinatário",
        xsd_required=True,
        help=u"Valor da Base de Cálculo do ICMS na UF do destinatário.")
    nfe_pFCPUFDest = fields.Monetary(
        digits=2, string="pFCPUFDest", xsd_required=True,
        help=(u"Percentual adicional inserido na alíquota interna da UF de"
              u"destino, relativo ao Fundo de Combate à Pobreza (FCP)"
              u"naquela UF."))
    nfe_pICMSUFDest = fields.Monetary(
        digits=2, string="pICMSUFDest", xsd_required=True,
        help=(u"Alíquota adotada nas operações internas na UF do destinatário"
              u"para o produto / mercadoria."))
    nfe_pICMSInter = fields.Selection(
        pICMSInterType,
        string="Alíquota interestadual das UF envolvidas:",
        xsd_required=True,
        help=(u"Alíquota interestadual das UF envolvidas"
              u"- 4% alíquota interestadual para produtos importados"
              u"- 7% para os Estados de origem do Sul e Sudeste (exceto ES),"
              u"destinado para os Estados do Norte e Nordeste  ou ES"
              u"- 12% para os demais casos."))
    nfe_pICMSInterPart = fields.Monetary(
        digits=2, string="Percentual de partilha para a UF do destinatário:",
        xsd_required=True,
        help=(u"Percentual de partilha para a UF do destinatário: - 40% em"
              u"2016; - 60% em 2017; - 80% em 2018; - 100% a partir de"
              u"2019."))
    nfe_vFCPUFDest = fields.Monetary(
        digits=2, 
        string="Valor do ICMS relativo ao Fundo de Combate à Pobreza",
        xsd_required=True,
        help=(u"Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) da"
              u"UF de destino."))
    nfe_vICMSUFDest = fields.Monetary(
        digits=2, 
        string="Valor do ICMS de partilha para a UF do destinatário",
        xsd_required=True,
        help=u"Valor do ICMS de partilha para a UF do destinatário.")
    nfe_vICMSUFRemet = fields.Monetary(
        digits=2, string="Valor do ICMS de partilha para a UF do remetente",
        xsd_required=True,
        help=(u"Valor do ICMS de partilha para a UF do remetente. Nota: A"
              u"partir de 2019, este valor será zero."))


class II(spec_models.AbstractSpecMixin):
    _description = u"Dados do Imposto de Importação"
    _name = 'nfe.v3_10.ii'
    _generateds_type = 'IIType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_vBC'

    nfe_vBC = fields.Monetary(
        digits=2, string="Base da BC do Imposto de Importação",
        xsd_required=True,
        help=u"Base da BC do Imposto de Importação")
    nfe_vDespAdu = fields.Monetary(
        digits=2, string="Valor das despesas aduaneiras",
        xsd_required=True,
        help=u"Valor das despesas aduaneiras")
    nfe_vII = fields.Monetary(
        digits=2, string="Valor do Imposto de Importação",
        xsd_required=True,
        help=u"Valor do Imposto de Importação")
    nfe_vIOF = fields.Monetary(
        digits=2, string="Valor do Imposto sobre Operações Financeiras",
        xsd_required=True,
        help=u"Valor do Imposto sobre Operações Financeiras")


class IPINT(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.ipint'
    _generateds_type = 'IPINTType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CST'

    nfe_CST = fields.Selection(
        CSTType71,
        string="Código da Situação Tributária do IPI:",
        xsd_required=True,
        help=u"Código da Situação Tributária do IPI:")


class IPITrib(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.ipitrib'
    _generateds_type = 'IPITribType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CST'

    nfe_choice20 = fields.Selection([
        ('nfe_vBC', 'vBC'),
        ('nfe_pIPI', 'pIPI'),
        ('nfe_qUnid', 'qUnid'),
        ('nfe_vUnid', 'vUnid')],
        "vBC/pIPI/qUnid/vUnid",
        default="nfe_vBC")
    nfe_CST = fields.Selection(
        CSTType70,
        string="Código da Situação Tributária do IPI:",
        xsd_required=True,
        help=u"Código da Situação Tributária do IPI:")
    nfe_vBC = fields.Monetary(
        digits=2, choice='20',
        string="Valor da BC do IPI", xsd_required=True,
        help=u"Valor da BC do IPI")
    nfe_pIPI = fields.Monetary(
        digits=2, choice='20',
        string="Alíquota do IPI", xsd_required=True,
        help=u"Alíquota do IPI")
    nfe_qUnid = fields.Monetary(
        digits=4, choice='20',
        string="Quantidade total na unidade padrão para tributação",
        xsd_required=True,
        help=u"Quantidade total na unidade padrão para tributação")
    nfe_vUnid = fields.Monetary(
        digits=4, choice='20',
        string="Valor por Unidade Tributável",
        xsd_required=True,
        help=(u"Valor por Unidade Tributável. Informar o valor do imposto Pauta"
              u"por unidade de medida."))
    nfe_vIPI = fields.Monetary(
        digits=2, string="Valor do IPI", xsd_required=True,
        help=u"Valor do IPI")


class IPI(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.ipi'
    _generateds_type = 'IPIType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_vIPIDevol'

    nfe_vIPIDevol = fields.Monetary(
        digits=2, string="Valor do IPI devolvido",
        xsd_required=True,
        help=u"Valor do IPI devolvido")


class ISSQN(spec_models.AbstractSpecMixin):
    _description = u"ISSQN"
    _name = 'nfe.v3_10.issqn'
    _generateds_type = 'ISSQNType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_vBC'

    nfe_vBC = fields.Monetary(
        digits=2, string="Valor da BC do ISSQN", xsd_required=True,
        help=u"Valor da BC do ISSQN")
    nfe_vAliq = fields.Monetary(
        digits=2, string="Alíquota do ISSQN", xsd_required=True,
        help=u"Alíquota do ISSQN")
    nfe_vISSQN = fields.Monetary(
        digits=2, string="Valor da do ISSQN", xsd_required=True,
        help=u"Valor da do ISSQN")
    nfe_cMunFG = fields.Char(
        string="Informar o município de ocorrência do fato gerador do ISSQN",
        xsd_required=True,
        help=(u"Informar o município de ocorrência do fato gerador do ISSQN."
              u"Utilizar a Tabela do IBGE (Anexo VII - Tabela de UF,"
              u"Município e País). “Atenção, não vincular com os campos"
              u"B12, C10 ou E10” v2.0"))
    nfe_cListServ = fields.Selection(
        TCListServ,
        string="cListServ", xsd_required=True,
        help=u"Tipo Código da Lista de Serviços LC 116/2003")
    nfe_vDeducao = fields.Monetary(
        digits=2, string="Valor dedução para redução da base de cálculo",
        help=u"Valor dedução para redução da base de cálculo")
    nfe_vOutro = fields.Monetary(
        digits=2, string="Valor outras retenções",
        help=u"Valor outras retenções")
    nfe_vDescIncond = fields.Monetary(
        digits=2, string="Valor desconto incondicionado",
        help=u"Valor desconto incondicionado")
    nfe_vDescCond = fields.Monetary(
        digits=2, string="Valor desconto condicionado",
        help=u"Valor desconto condicionado")
    nfe_vISSRet = fields.Monetary(
        digits=2, string="Valor Retenção ISS",
        help=u"Valor Retenção ISS")
    nfe_indISS = fields.Selection(
        indISSType,
        string="Exibilidade do ISS:1", xsd_required=True,
        help=u"Exibilidade do ISS")
    nfe_cServico = fields.Char(
        string="Código do serviço prestado dentro do município",
        help=u"Código do serviço prestado dentro do município")
    nfe_cMun = fields.Char(
        string="Código do Município de Incidência do Imposto",
        help=u"Código do Município de Incidência do Imposto")
    nfe_cPais = fields.Char(
        string="Código de Pais",
        help=u"Código de Pais")
    nfe_nProcesso = fields.Char(
        string="nProcesso",
        help=(u"Número do Processo administrativo ou judicial de suspenção do"
              u"processo"))
    nfe_indIncentivo = fields.Selection(
        indIncentivoType,
        string="Indicador de Incentivo Fiscal",
        xsd_required=True,
        help=u"Indicador de Incentivo Fiscal. 1=Sim; 2=Não")


class ISSQNtot(spec_models.AbstractSpecMixin):
    _description = u"Totais referentes ao ISSQN"
    _name = 'nfe.v3_10.issqntot'
    _generateds_type = 'ISSQNtotType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_vServ'

    nfe_vServ = fields.Monetary(
        digits=2, string="Valor Total dos Serviços sob não",
        help=(u"Valor Total dos Serviços sob não-incidência ou não tributados"
              u"pelo ICMS"))
    nfe_vBC = fields.Monetary(
        digits=2, string="Base de Cálculo do ISS",
        help=u"Base de Cálculo do ISS")
    nfe_vISS = fields.Monetary(
        digits=2, string="Valor Total do ISS",
        help=u"Valor Total do ISS")
    nfe_vPIS = fields.Monetary(
        digits=2, string="Valor do PIS sobre serviços",
        help=u"Valor do PIS sobre serviços")
    nfe_vCOFINS = fields.Monetary(
        digits=2, string="Valor do COFINS sobre serviços",
        help=u"Valor do COFINS sobre serviços")
    nfe_dCompet = fields.Char(
        string="Data da prestação do serviço",
        xsd_required=True,
        help=u"Data da prestação do serviço  (AAAA-MM-DD)")
    nfe_vDeducao = fields.Monetary(
        digits=2, string="Valor dedução para redução da base de cálculo",
        help=u"Valor dedução para redução da base de cálculo")
    nfe_vOutro = fields.Monetary(
        digits=2, string="Valor outras retenções",
        help=u"Valor outras retenções")
    nfe_vDescIncond = fields.Monetary(
        digits=2, string="Valor desconto incondicionado",
        help=u"Valor desconto incondicionado")
    nfe_vDescCond = fields.Monetary(
        digits=2, string="Valor desconto condicionado",
        help=u"Valor desconto condicionado")
    nfe_vISSRet = fields.Monetary(
        digits=2, string="Valor Total Retenção ISS",
        help=u"Valor Total Retenção ISS")
    nfe_cRegTrib = fields.Selection(
        cRegTribType,
        string="Código do regime especial de tributação",
        help=u"Código do regime especial de tributação")


class NFref(spec_models.AbstractSpecMixin):
    _description = u"Grupo de infromações da NF referenciada"
    _name = 'nfe.v3_10.nfref'
    _generateds_type = 'NFrefType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_refNFe'

    nfe_NFref_ide_id = fields.Many2one(
        "nfe.v3_10.ide")
    nfe_choice4 = fields.Selection([
        ('nfe_refNFe', 'refNFe'),
        ('nfe_refNF', 'refNF'),
        ('nfe_refNFP', 'refNFP'),
        ('nfe_refCTe', 'refCTe'),
        ('nfe_refECF', 'refECF')],
        "refNFe/refNF/refNFP/refCTe/refECF",
        default="nfe_refNFe")
    nfe_refNFe = fields.Char(
        choice='4',
        string="Chave de acesso das NF",
        xsd_required=True,
        help=(u"Chave de acesso das NF-e referenciadas. Chave de acesso"
              u"compostas por Código da UF (tabela do IBGE) + AAMM da"
              u"emissão + CNPJ do Emitente + modelo, série e número da NF-e"
              u"Referenciada + Código Numérico + DV."))
    nfe_refNF = fields.Many2one(
        "nfe.v3_10.refnf",
        choice='4',
        string="Dados da NF modelo 1/1A referenciada",
        xsd_required=True,
        help=u"Dados da NF modelo 1/1A referenciada")
    nfe_refNFP = fields.Many2one(
        "nfe.v3_10.refnfp",
        choice='4',
        string="Grupo com as informações NF de produtor referenciada",
        xsd_required=True,
        help=u"Grupo com as informações NF de produtor referenciada")
    nfe_refCTe = fields.Char(
        choice='4',
        string="Utilizar esta TAG para referenciar um CT",
        xsd_required=True,
        help=(u"Utilizar esta TAG para referenciar um CT-e emitido"
              u"anteriormente, vinculada a NF-e atual"))
    nfe_refECF = fields.Many2one(
        "nfe.v3_10.refecf",
        choice='4',
        string="Grupo do Cupom Fiscal vinculado à NF",
        xsd_required=True,
        help=u"Grupo do Cupom Fiscal vinculado à NF-e")


class PISAliq(spec_models.AbstractSpecMixin):
    _description = (u"Código de Situação Tributária do PIS."
                    u"01 – Operação Tributável - Base de Cálculo = Valor da"
                    u"Operação"
                    u"Alíquota Normal (Cumulativo/Não Cumulativo);"
                    u"02 - Operação Tributável - Base de Calculo = Valor da"
                    u"Operação"
                    u"(Alíquota Diferenciada);")
    _name = 'nfe.v3_10.pisaliq'
    _generateds_type = 'PISAliqType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CST'

    nfe_CST = fields.Selection(
        CSTType41,
        string="Código de Situação Tributária do PIS",
        xsd_required=True,
        help=u"Código de Situação Tributária do PIS.")
    nfe_vBC = fields.Monetary(
        digits=2, string="Valor da BC do PIS", xsd_required=True,
        help=u"Valor da BC do PIS")
    nfe_pPIS = fields.Monetary(
        digits=2, string="Alíquota do PIS (em percentual)",
        xsd_required=True,
        help=u"Alíquota do PIS (em percentual)")
    nfe_vPIS = fields.Monetary(
        digits=2, string="Valor do PIS", xsd_required=True,
        help=u"Valor do PIS")


class PISNT(spec_models.AbstractSpecMixin):
    _description = (u"Código de Situação Tributária do PIS."
                    u"04 - Operação Tributável - Tributação Monofásica -"
                    u"(Alíquota Zero);"
                    u"06 - Operação Tributável - Alíquota Zero;"
                    u"07 - Operação Isenta da contribuição;"
                    u"08 - Operação Sem Incidência da contribuição;"
                    u"09 - Operação com suspensão da contribuição;")
    _name = 'nfe.v3_10.pisnt'
    _generateds_type = 'PISNTType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CST'

    nfe_CST = fields.Selection(
        CSTType43,
        string="Código de Situação Tributária do PIS",
        xsd_required=True,
        help=u"Código de Situação Tributária do PIS.")


class PISOutr(spec_models.AbstractSpecMixin):
    _description = (u"Código de Situação Tributária do PIS."
                    u"99 - Outras Operações.")
    _name = 'nfe.v3_10.pisoutr'
    _generateds_type = 'PISOutrType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CST'

    nfe_choice13 = fields.Selection([
        ('nfe_vBC', 'vBC'),
        ('nfe_pPIS', 'pPIS'),
        ('nfe_qBCProd', 'qBCProd'),
        ('nfe_vAliqProd', 'vAliqProd')],
        "vBC/pPIS/qBCProd/vAliqProd",
        default="nfe_vBC")
    nfe_CST = fields.Selection(
        CSTType44,
        string="Código de Situação Tributária do PIS",
        xsd_required=True,
        help=(u"Código de Situação Tributária do PIS."
              u"99 - Outras Operações."))
    nfe_vBC = fields.Monetary(
        digits=2, choice='13',
        string="Valor da BC do PIS", xsd_required=True,
        help=u"Valor da BC do PIS")
    nfe_pPIS = fields.Monetary(
        digits=2, choice='13',
        string="Alíquota do PIS (em percentual)",
        xsd_required=True,
        help=u"Alíquota do PIS (em percentual)")
    nfe_qBCProd = fields.Monetary(
        digits=4, choice='13',
        string="Quantidade Vendida (NT2011/004) ",
        xsd_required=True,
        help=u"Quantidade Vendida (NT2011/004)")
    nfe_vAliqProd = fields.Monetary(
        digits=4, choice='13',
        string="Alíquota do PIS", xsd_required=True,
        help=u"Alíquota do PIS (em reais) (NT2011/004)")
    nfe_vPIS = fields.Monetary(
        digits=2, string="Valor do PIS", xsd_required=True,
        help=u"Valor do PIS")


class PISQtde(spec_models.AbstractSpecMixin):
    _description = (u"Código de Situação Tributária do PIS."
                    u"03 - Operação Tributável - Base de Calculo ="
                    u"Quantidade Vendida x"
                    u"Alíquota por Unidade de Produto;")
    _name = 'nfe.v3_10.pisqtde'
    _generateds_type = 'PISQtdeType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CST'

    nfe_CST = fields.Selection(
        CSTType42,
        string="Código de Situação Tributária do PIS",
        xsd_required=True,
        help=u"Código de Situação Tributária do PIS.")
    nfe_qBCProd = fields.Monetary(
        digits=4, string="Quantidade Vendida  (NT2011/004)",
        xsd_required=True,
        help=u"Quantidade Vendida  (NT2011/004)")
    nfe_vAliqProd = fields.Monetary(
        digits=4, string="Alíquota do PIS", xsd_required=True,
        help=u"Alíquota do PIS (em reais) (NT2011/004)")
    nfe_vPIS = fields.Monetary(
        digits=2, string="Valor do PIS", xsd_required=True,
        help=u"Valor do PIS")


class PISST(spec_models.AbstractSpecMixin):
    _description = u"Dados do PIS Substituição Tributária"
    _name = 'nfe.v3_10.pisst'
    _generateds_type = 'PISSTType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_vBC'

    nfe_choice14 = fields.Selection([
        ('nfe_vBC', 'vBC'),
        ('nfe_pPIS', 'pPIS'),
        ('nfe_qBCProd', 'qBCProd'),
        ('nfe_vAliqProd', 'vAliqProd')],
        "vBC/pPIS/qBCProd/vAliqProd",
        default="nfe_vBC")
    nfe_vBC = fields.Monetary(
        digits=2, choice='14',
        string="Valor da BC do PIS ST", xsd_required=True,
        help=u"Valor da BC do PIS ST")
    nfe_pPIS = fields.Monetary(
        digits=2, choice='14',
        string="Alíquota do PIS ST", xsd_required=True,
        help=u"Alíquota do PIS ST (em percentual)")
    nfe_qBCProd = fields.Monetary(
        digits=4, choice='14',
        string="Quantidade Vendida ", xsd_required=True,
        help=u"Quantidade Vendida")
    nfe_vAliqProd = fields.Monetary(
        digits=4, choice='14',
        string="Alíquota do PIS ST (em reais)",
        xsd_required=True,
        help=u"Alíquota do PIS ST (em reais)")
    nfe_vPIS = fields.Monetary(
        digits=2, string="Valor do PIS ST", xsd_required=True,
        help=u"Valor do PIS ST")


class PIS(spec_models.AbstractSpecMixin):
    _description = u"Dados do PIS"
    _name = 'nfe.v3_10.pis'
    _generateds_type = 'PISType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_PISAliq'

    nfe_choice12 = fields.Selection([
        ('nfe_PISAliq', 'PISAliq'),
        ('nfe_PISQtde', 'PISQtde'),
        ('nfe_PISNT', 'PISNT'),
        ('nfe_PISOutr', 'PISOutr')],
        "PISAliq/PISQtde/PISNT/PISOutr",
        default="nfe_PISAliq")
    nfe_PISAliq = fields.Many2one(
        "nfe.v3_10.pisaliq",
        choice='12',
        string="Código de Situação Tributária do PIS",
        xsd_required=True,
        help=(u"Código de Situação Tributária do PIS."
              u"01 – Operação Tributável - Base de Cálculo = Valor da Operação"
              u"Alíquota Normal (Cumulativo/Não Cumulativo);"
              u"02 - Operação Tributável - Base de Calculo = Valor da Operação"
              u"(Alíquota Diferenciada);"))
    nfe_PISQtde = fields.Many2one(
        "nfe.v3_10.pisqtde",
        choice='12',
        string="Código de Situação Tributária do PIS",
        xsd_required=True,
        help=(u"Código de Situação Tributária do PIS."
              u"03 - Operação Tributável - Base de Calculo = Quantidade Vendida"
              u"x Alíquota por Unidade de Produto;"))
    nfe_PISNT = fields.Many2one(
        "nfe.v3_10.pisnt",
        choice='12',
        string="Código de Situação Tributária do PIS",
        xsd_required=True,
        help=(u"Código de Situação Tributária do PIS."
              u"04 - Operação Tributável - Tributação Monofásica - (Alíquota"
              u"Zero);"
              u"06 - Operação Tributável - Alíquota Zero;"
              u"07 - Operação Isenta da contribuição;"
              u"08 - Operação Sem Incidência da contribuição;"
              u"09 - Operação com suspensão da contribuição;"))
    nfe_PISOutr = fields.Many2one(
        "nfe.v3_10.pisoutr",
        choice='12',
        string="Código de Situação Tributária do PIS",
        xsd_required=True,
        help=(u"Código de Situação Tributária do PIS."
              u"99 - Outras Operações."))


class TConsReciNFe(spec_models.AbstractSpecMixin):
    _description = (u"Tipo Pedido de Consulta do Recido do Lote de Notas Fiscais"
                    u"Eletrônicas")
    _name = 'nfe.v3_10.tconsrecinfe'
    _generateds_type = 'TConsReciNFe'
    _concrete_class = None
    _concrete_rec_name = 'nfe_versao'

    nfe_versao = fields.Char(
        string="versao", xsd_required=True)
    nfe_tpAmb = fields.Selection(
        TAmb,
        string="Identificação do Ambiente:",
        xsd_required=True,
        help=u"Tipo Ambiente")
    nfe_nRec = fields.Char(
        string="Número do Recibo", xsd_required=True,
        help=u"Número do Recibo")


class TEnderEmi(spec_models.AbstractSpecMixin):
    _description = (u"Tipo Dados do Endereço do Emitente  // 24/10/08 -"
                    u"desmembrado / tamanho"
                    u"mínimo")
    _name = 'nfe.v3_10.tenderemi'
    _generateds_type = 'TEnderEmi'
    _concrete_class = None
    _concrete_rec_name = 'nfe_xLgr'

    nfe_xLgr = fields.Char(
        string="Logradouro", xsd_required=True,
        help=u"Logradouro")
    nfe_nro = fields.Char(
        string="Número", xsd_required=True,
        help=u"Número")
    nfe_xCpl = fields.Char(
        string="Complemento",
        help=u"Complemento")
    nfe_xBairro = fields.Char(
        string="Bairro", xsd_required=True,
        help=u"Bairro")
    nfe_cMun = fields.Char(
        string="Código do município", xsd_required=True,
        help=u"Código do município")
    nfe_xMun = fields.Char(
        string="Nome do município", xsd_required=True,
        help=u"Nome do município")
    nfe_UF = fields.Selection(
        TUfEmi,
        string="Sigla da UF", xsd_required=True,
        help=u"Tipo Sigla da UF de emissor // acrescentado em 24/10/08")
    nfe_CEP = fields.Char(
        string="CEP - NT 2011/004", xsd_required=True,
        help=u"CEP - NT 2011/004")
    nfe_cPais = fields.Selection(
        cPaisType62,
        string="Código do país",
        help=u"Código do país")
    nfe_xPais = fields.Selection(
        xPaisType63,
        string="Nome do país",
        help=u"Nome do país")
    nfe_fone = fields.Char(
        string="Preencher com Código DDD + número do telefone",
        help=u"Preencher com Código DDD + número do telefone (v.2.0)")


class TEndereco(spec_models.AbstractSpecMixin):
    _description = u"Tipo Dados do Endereço  // 24/10/08 - tamanho mínimo"
    _name = 'nfe.v3_10.tendereco'
    _generateds_type = 'TEndereco'
    _concrete_class = None
    _concrete_rec_name = 'nfe_xLgr'

    nfe_xLgr = fields.Char(
        string="Logradouro", xsd_required=True,
        help=u"Logradouro")
    nfe_nro = fields.Char(
        string="Número", xsd_required=True,
        help=u"Número")
    nfe_xCpl = fields.Char(
        string="Complemento",
        help=u"Complemento")
    nfe_xBairro = fields.Char(
        string="Bairro", xsd_required=True,
        help=u"Bairro")
    nfe_cMun = fields.Char(
        string="Código do município", xsd_required=True,
        help=(u"Código do município (utilizar a tabela do IBGE), informar"
              u"9999999 para operações com o exterior."))
    nfe_xMun = fields.Char(
        string="Nome do município", xsd_required=True,
        help=(u"Nome do município, informar EXTERIOR para operações com o"
              u"exterior."))
    nfe_UF = fields.Selection(
        TUf,
        string="Sigla da UF", xsd_required=True,
        help=u"Tipo Sigla da UF")
    nfe_CEP = fields.Char(
        string="CEP",
        help=u"CEP")
    nfe_cPais = fields.Char(
        string="Código de Pais",
        help=u"Código de Pais")
    nfe_xPais = fields.Char(
        string="Nome do país",
        help=u"Nome do país")
    nfe_fone = fields.Char(
        string="Telefone",
        help=(u"Telefone, preencher com Código DDD + número do telefone , nas"
              u"operações com exterior é permtido informar o código do país"
              u"+ código da localidade + número do telefone"))


class TEnviNFe(spec_models.AbstractSpecMixin):
    _description = (u"Tipo Pedido de Concessão de Autorização da Nota Fiscal"
                    u"Eletrônica")
    _name = 'nfe.v3_10.tenvinfe'
    _generateds_type = 'TEnviNFe'
    _concrete_class = None
    _concrete_rec_name = 'nfe_versao'

    nfe_versao = fields.Char(
        string="versao", xsd_required=True)
    nfe_idLote = fields.Char(
        string="idLote", xsd_required=True)
    nfe_indSinc = fields.Selection(
        indSincType,
        string="Indicador de processamento síncrono",
        xsd_required=True,
        help=u"Indicador de processamento síncrono. 0=NÃO; 1=SIM=Síncrono")
    nfe_NFe = fields.One2many(
        "nfe.v3_10.tnfe",
        "nfe_NFe_TEnviNFe_id",
        string="NFe", xsd_required=True
    )


class TIpi(spec_models.AbstractSpecMixin):
    _description = u"Tipo: Dados do IPI"
    _name = 'nfe.v3_10.tipi'
    _generateds_type = 'TIpi'
    _concrete_class = None
    _concrete_rec_name = 'nfe_clEnq'

    nfe_choice3 = fields.Selection([
        ('nfe_IPITrib', 'IPITrib'),
        ('nfe_IPINT', 'IPINT')],
        "IPITrib/IPINT",
        default="nfe_IPITrib")
    nfe_clEnq = fields.Char(
        string="Classe de Enquadramento do IPI para Cigarros e Bebidas",
        help=u"Classe de Enquadramento do IPI para Cigarros e Bebidas")
    nfe_CNPJProd = fields.Char(
        string="CNPJ do produtor da mercadoria",
        help=(u"CNPJ do produtor da mercadoria, quando diferente do emitente."
              u"Somente para os casos de exportação direta ou indireta."))
    nfe_cSelo = fields.Char(
        string="Código do selo de controle do IPI",
        help=u"Código do selo de controle do IPI")
    nfe_qSelo = fields.Char(
        string="Quantidade de selo de controle do IPI",
        help=u"Quantidade de selo de controle do IPI")
    nfe_cEnq = fields.Char(
        string="Código de Enquadramento Legal do IPI",
        xsd_required=True,
        help=(u"Código de Enquadramento Legal do IPI (tabela a ser criada pela"
              u"RFB)"))
    nfe_IPITrib = fields.Many2one(
        "nfe.v3_10.ipitrib",
        choice='3',
        string="IPITrib", xsd_required=True)
    nfe_IPINT = fields.Many2one(
        "nfe.v3_10.ipint",
        choice='3',
        string="IPINT", xsd_required=True)


class TLocal(spec_models.AbstractSpecMixin):
    _description = (u"Tipo Dados do Local de Retirada ou Entrega // 24/10/08 -"
                    u"tamanho mínimo"
                    u"// v2.0")
    _name = 'nfe.v3_10.tlocal'
    _generateds_type = 'TLocal'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CNPJ'

    nfe_choice2 = fields.Selection([
        ('nfe_CNPJ', 'CNPJ'),
        ('nfe_CPF', 'CPF')],
        "CNPJ/CPF",
        default="nfe_CNPJ")
    nfe_CNPJ = fields.Char(
        choice='2',
        string="CNPJ", xsd_required=True,
        help=u"CNPJ")
    nfe_CPF = fields.Char(
        choice='2',
        string="CPF (v2.0)", xsd_required=True,
        help=u"CPF (v2.0)")
    nfe_xLgr = fields.Char(
        string="Logradouro", xsd_required=True,
        help=u"Logradouro")
    nfe_nro = fields.Char(
        string="Número", xsd_required=True,
        help=u"Número")
    nfe_xCpl = fields.Char(
        string="Complemento",
        help=u"Complemento")
    nfe_xBairro = fields.Char(
        string="Bairro", xsd_required=True,
        help=u"Bairro")
    nfe_cMun = fields.Char(
        string="Código do município", xsd_required=True,
        help=u"Código do município (utilizar a tabela do IBGE)")
    nfe_xMun = fields.Char(
        string="Nome do município", xsd_required=True,
        help=u"Nome do município")
    nfe_UF = fields.Selection(
        TUf,
        string="Sigla da UF", xsd_required=True,
        help=u"Tipo Sigla da UF")


class TNFe(spec_models.AbstractSpecMixin):
    _description = u"Tipo Nota Fiscal Eletrônica"
    _name = 'nfe.v3_10.tnfe'
    _generateds_type = 'TNFe'
    _concrete_class = None
    _concrete_rec_name = 'nfe_infNFe'

    nfe_NFe_TEnviNFe_id = fields.Many2one(
        "nfe.v3_10.tenvinfe")
    nfe_infNFe = fields.Many2one(
        "nfe.v3_10.infnfe",
        string="Informações da Nota Fiscal eletrônica",
        xsd_required=True,
        help=u"Informações da Nota Fiscal eletrônica")
    nfe_infNFeSupl = fields.Many2one(
        "nfe.v3_10.infnfesupl",
        string="Informações suplementares Nota Fiscal",
        help=u"Informações suplementares Nota Fiscal")
    nfe_Signature = fields.Char(
        string="Signature", xsd_required=True)


class TNfeProc(spec_models.AbstractSpecMixin):
    _description = u"Tipo da NF-e processada"
    _name = 'nfe.v3_10.tnfeproc'
    _generateds_type = 'TNfeProc'
    _concrete_class = None
    _concrete_rec_name = 'nfe_versao'

    nfe_versao = fields.Char(
        string="versao", xsd_required=True)
    nfe_NFe = fields.Many2one(
        "nfe.v3_10.tnfe",
        string="NFe", xsd_required=True)
    nfe_protNFe = fields.Many2one(
        "nfe.v3_10.tprotnfe",
        string="protNFe", xsd_required=True)


class TProtNFe(spec_models.AbstractSpecMixin):
    _description = (u"Tipo Protocolo de status resultado do processamento da"
                    u"NF-e")
    _name = 'nfe.v3_10.tprotnfe'
    _generateds_type = 'TProtNFe'
    _concrete_class = None
    _concrete_rec_name = 'nfe_versao'

    nfe_protNFe_TRetConsReciNFe_id = fields.Many2one(
        "nfe.v3_10.tretconsrecinfe")
    nfe_versao = fields.Char(
        string="versao", xsd_required=True)
    nfe_infProt = fields.Many2one(
        "nfe.v3_10.infprot",
        string="Dados do protocolo de status",
        xsd_required=True,
        help=u"Dados do protocolo de status")
    nfe_Signature = fields.Char(
        string="Signature")


class TRetConsReciNFe(spec_models.AbstractSpecMixin):
    _description = (u"Tipo Retorno do Pedido de  Consulta do Recido do Lote de"
                    u"Notas Fiscais"
                    u"Eletrônicas")
    _name = 'nfe.v3_10.tretconsrecinfe'
    _generateds_type = 'TRetConsReciNFe'
    _concrete_class = None
    _concrete_rec_name = 'nfe_versao'

    nfe_versao = fields.Char(
        string="versao", xsd_required=True)
    nfe_tpAmb = fields.Selection(
        TAmb,
        string="Identificação do Ambiente:",
        xsd_required=True,
        help=u"Tipo Ambiente")
    nfe_verAplic = fields.Char(
        string="Versão do Aplicativo que processou a NF",
        xsd_required=True,
        help=u"Versão do Aplicativo que processou a NF-e")
    nfe_nRec = fields.Char(
        string="Número do Recibo Consultado",
        xsd_required=True,
        help=u"Número do Recibo Consultado")
    nfe_cStat = fields.Char(
        string="Código do status da mensagem enviada",
        xsd_required=True,
        help=u"Código do status da mensagem enviada.")
    nfe_xMotivo = fields.Char(
        string="Descrição literal do status do serviço solicitado",
        xsd_required=True,
        help=u"Descrição literal do status do serviço solicitado.")
    nfe_cUF = fields.Selection(
        TCodUfIBGE,
        string="código da UF de atendimento",
        xsd_required=True,
        help=u"Tipo Código da UF da tabela do IBGE")
    nfe_dhRecbto = fields.Char(
        string="Data e hora de processamento",
        xsd_required=True,
        help=(u"Data e hora de processamento, no formato AAAA-MM-"
              u"DDTHH:MM:SSTZD. Em caso de Rejeição, com data e hora do"
              u"recebimento do Lote de NF-e enviado."))
    nfe_cMsg = fields.Char(
        string="Código da Mensagem (v2.0) ",
        help=(u"Código da Mensagem (v2.0)"
              u"alterado para tamanho variavel 1-4. (NT2011/004)"))
    nfe_xMsg = fields.Char(
        string="Mensagem da SEFAZ para o emissor",
        help=u"Mensagem da SEFAZ para o emissor. (v2.0)")
    nfe_protNFe = fields.One2many(
        "nfe.v3_10.tprotnfe",
        "nfe_protNFe_TRetConsReciNFe_id",
        string="Protocolo de status resultado do processamento da NF",
        help=u"Protocolo de status resultado do processamento da NF-e"
    )


class TRetEnviNFe(spec_models.AbstractSpecMixin):
    _description = (u"Tipo Retorno do Pedido de Autorização da Nota Fiscal"
                    u"Eletrônica")
    _name = 'nfe.v3_10.tretenvinfe'
    _generateds_type = 'TRetEnviNFe'
    _concrete_class = None
    _concrete_rec_name = 'nfe_versao'

    nfe_choice1 = fields.Selection([
        ('nfe_infRec', 'infRec'),
        ('nfe_protNFe', 'protNFe')],
        "infRec/protNFe",
        default="nfe_infRec")
    nfe_versao = fields.Char(
        string="versao", xsd_required=True)
    nfe_tpAmb = fields.Selection(
        TAmb,
        string="Identificação do Ambiente:",
        xsd_required=True,
        help=u"Tipo Ambiente")
    nfe_verAplic = fields.Char(
        string="Versão do Aplicativo que recebeu o Lote",
        xsd_required=True,
        help=u"Versão do Aplicativo que recebeu o Lote.")
    nfe_cStat = fields.Char(
        string="Código do status da mensagem enviada",
        xsd_required=True,
        help=u"Código do status da mensagem enviada.")
    nfe_xMotivo = fields.Char(
        string="Descrição literal do status do serviço solicitado",
        xsd_required=True,
        help=u"Descrição literal do status do serviço solicitado.")
    nfe_cUF = fields.Selection(
        TCodUfIBGE,
        string="código da UF de atendimento",
        xsd_required=True,
        help=u"Tipo Código da UF da tabela do IBGE")
    nfe_dhRecbto = fields.Char(
        string="Data e hora do recebimento",
        xsd_required=True,
        help=u"Data e hora do recebimento, no formato AAAA-MM-DDTHH:MM:SSTZD")
    nfe_infRec = fields.Many2one(
        "nfe.v3_10.infrec",
        choice='1',
        string="Dados do Recibo do Lote",
        help=u"Dados do Recibo do Lote")
    nfe_protNFe = fields.Many2one(
        "nfe.v3_10.tprotnfe",
        choice='1',
        string="Protocolo de status resultado do processamento sincrono da NFC",
        help=(u"Protocolo de status resultado do processamento sincrono da"
              u"NFC-e"))


class TVeiculo(spec_models.AbstractSpecMixin):
    _description = u"Tipo Dados do Veículo"
    _name = 'nfe.v3_10.tveiculo'
    _generateds_type = 'TVeiculo'
    _concrete_class = None
    _concrete_rec_name = 'nfe_placa'

    nfe_reboque_transp_id = fields.Many2one(
        "nfe.v3_10.transp")
    nfe_placa = fields.Char(
        string="Placa do veículo (NT2011/004)",
        xsd_required=True,
        help=u"Placa do veículo (NT2011/004)")
    nfe_UF = fields.Selection(
        TUf,
        string="Sigla da UF", xsd_required=True,
        help=u"Tipo Sigla da UF")
    nfe_RNTC = fields.Char(
        string="Registro Nacional de Transportador de Carga",
        help=u"Registro Nacional de Transportador de Carga (ANTT)")


class adi(spec_models.AbstractSpecMixin):
    _description = u"Adições (NT 2011/004)"
    _name = 'nfe.v3_10.adi'
    _generateds_type = 'adiType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_nAdicao'

    nfe_adi_DI_id = fields.Many2one(
        "nfe.v3_10.di")
    nfe_nAdicao = fields.Char(
        string="Número da Adição", xsd_required=True,
        help=u"Número da Adição")
    nfe_nSeqAdic = fields.Char(
        string="Número seqüencial do item dentro da Adição",
        xsd_required=True,
        help=u"Número seqüencial do item dentro da Adição")
    nfe_cFabricante = fields.Char(
        string="Código do fabricante estrangeiro",
        xsd_required=True,
        help=(u"Código do fabricante estrangeiro (usado nos sistemas internos"
              u"de informação do emitente da NF-e)"))
    nfe_vDescDI = fields.Monetary(
        digits=2, string="Valor do desconto do item da DI – adição",
        help=u"Valor do desconto do item da DI – adição")
    nfe_nDraw = fields.Char(
        string="Número do ato concessório de Drawback",
        help=u"Número do ato concessório de Drawback")


class arma(spec_models.AbstractSpecMixin):
    _description = u"Armamentos"
    _name = 'nfe.v3_10.arma'
    _generateds_type = 'armaType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_tpArma'

    nfe_arma_prod_id = fields.Many2one(
        "nfe.v3_10.prod")
    nfe_tpArma = fields.Selection(
        tpArmaType,
        string="Indicador do tipo de arma de fogo",
        xsd_required=True,
        help=(u"Indicador do tipo de arma de fogo (0 - Uso permitido; 1 - Uso"
              u"restrito)"))
    nfe_nSerie = fields.Char(
        string="Número de série da arma",
        xsd_required=True,
        help=u"Número de série da arma")
    nfe_nCano = fields.Char(
        string="Número de série do cano",
        xsd_required=True,
        help=u"Número de série do cano")
    nfe_descr = fields.Char(
        string="Descrição completa da arma",
        xsd_required=True,
        help=(u"Descrição completa da arma, compreendendo: calibre, marca,"
              u"capacidade, tipo de funcionamento, comprimento e demais"
              u"elementos que permitam a sua perfeita identificação."))


class autXML(spec_models.AbstractSpecMixin):
    _description = u"Pessoas autorizadas para o download do XML da NF-e"
    _name = 'nfe.v3_10.autxml'
    _generateds_type = 'autXMLType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CNPJ'

    nfe_autXML_infNFe_id = fields.Many2one(
        "nfe.v3_10.infnfe")
    nfe_choice8 = fields.Selection([
        ('nfe_CNPJ', 'CNPJ'),
        ('nfe_CPF', 'CPF')],
        "CNPJ/CPF",
        default="nfe_CNPJ")
    nfe_CNPJ = fields.Char(
        choice='8',
        string="CNPJ Autorizado", xsd_required=True,
        help=u"CNPJ Autorizado")
    nfe_CPF = fields.Char(
        choice='8',
        string="CPF Autorizado", xsd_required=True,
        help=u"CPF Autorizado")


class avulsa(spec_models.AbstractSpecMixin):
    _description = u"Emissão de avulsa, informar os dados do Fisco emitente"
    _name = 'nfe.v3_10.avulsa'
    _generateds_type = 'avulsaType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CNPJ'

    nfe_CNPJ = fields.Char(
        string="CNPJ do Órgão emissor", xsd_required=True,
        help=u"CNPJ do Órgão emissor")
    nfe_xOrgao = fields.Char(
        string="Órgão emitente", xsd_required=True,
        help=u"Órgão emitente")
    nfe_matr = fields.Char(
        string="Matrícula do agente", xsd_required=True,
        help=u"Matrícula do agente")
    nfe_xAgente = fields.Char(
        string="Nome do agente", xsd_required=True,
        help=u"Nome do agente")
    nfe_fone = fields.Char(
        string="Telefone",
        help=u"Telefone")
    nfe_UF = fields.Selection(
        TUfEmi,
        string="Sigla da Unidade da Federação",
        xsd_required=True,
        help=u"Tipo Sigla da UF de emissor // acrescentado em 24/10/08")
    nfe_nDAR = fields.Char(
        string="Número do Documento de Arrecadação de Receita",
        help=u"Número do Documento de Arrecadação de Receita")
    nfe_dEmi = fields.Char(
        string="Data de emissão do DAR (AAAA",
        help=u"Data de emissão do DAR (AAAA-MM-DD)")
    nfe_vDAR = fields.Monetary(
        digits=2, string="Valor Total constante no DAR",
        help=u"Valor Total constante no DAR")
    nfe_repEmi = fields.Char(
        string="Repartição Fiscal emitente",
        xsd_required=True,
        help=u"Repartição Fiscal emitente")
    nfe_dPag = fields.Char(
        string="Data de pagamento do DAR (AAAA",
        help=u"Data de pagamento do DAR (AAAA-MM-DD)")


class cana(spec_models.AbstractSpecMixin):
    _description = u"Informações de registro aquisições de cana"
    _name = 'nfe.v3_10.cana'
    _generateds_type = 'canaType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_safra'

    nfe_safra = fields.Char(
        string="Identificação da safra",
        xsd_required=True,
        help=u"Identificação da safra")
    nfe_ref = fields.Char(
        string="Mês e Ano de Referência", xsd_required=True,
        help=u"Mês e Ano de Referência, formato: MM/AAAA")
    nfe_forDia = fields.One2many(
        "nfe.v3_10.fordia",
        "nfe_forDia_cana_id",
        string="Fornecimentos diários",
        xsd_required=True,
        help=u"Fornecimentos diários"
    )
    nfe_qTotMes = fields.Monetary(
        digits=0, string="Total do mês", xsd_required=True,
        help=u"Total do mês")
    nfe_qTotAnt = fields.Monetary(
        digits=0, string="Total Anterior", xsd_required=True,
        help=u"Total Anterior")
    nfe_qTotGer = fields.Monetary(
        digits=0, string="Total Geral", xsd_required=True,
        help=u"Total Geral")
    nfe_deduc = fields.One2many(
        "nfe.v3_10.deduc",
        "nfe_deduc_cana_id",
        string="Deduções - Taxas e Contribuições",
        help=u"Deduções - Taxas e Contribuições"
    )
    nfe_vFor = fields.Monetary(
        digits=2, string="Valor  dos fornecimentos",
        xsd_required=True,
        help=u"Valor  dos fornecimentos")
    nfe_vTotDed = fields.Monetary(
        digits=2, string="Valor Total das Deduções",
        xsd_required=True,
        help=u"Valor Total das Deduções")
    nfe_vLiqFor = fields.Monetary(
        digits=2, string="Valor Líquido dos fornecimentos",
        xsd_required=True,
        help=u"Valor Líquido dos fornecimentos")


class card(spec_models.AbstractSpecMixin):
    _description = u"Grupo de Cartões"
    _name = 'nfe.v3_10.card'
    _generateds_type = 'cardType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_tpIntegra'

    nfe_tpIntegra = fields.Selection(
        tpIntegraType,
        string="tpIntegra",
        help=(u"Tipo de Integração do processo de pagamento com o sistema de"
              u"automação da empresa/"))
    nfe_CNPJ = fields.Char(
        string="CNPJ da credenciadora de cartão de crédito/débito",
        help=u"CNPJ da credenciadora de cartão de crédito/débito")
    nfe_tBand = fields.Selection(
        tBandType,
        string="tBand",
        help=u"Bandeira da operadora de cartão de crédito/débito")
    nfe_cAut = fields.Char(
        string="Número de autorização da operação cartão de crédito/débito",
        help=u"Número de autorização da operação cartão de crédito/débito")


class cobr(spec_models.AbstractSpecMixin):
    _description = u"Dados da cobrança da NF-e"
    _name = 'nfe.v3_10.cobr'
    _generateds_type = 'cobrType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_fat'

    nfe_fat = fields.Many2one(
        "nfe.v3_10.fat",
        string="Dados da fatura",
        help=u"Dados da fatura")
    nfe_dup = fields.One2many(
        "nfe.v3_10.dup",
        "nfe_dup_cobr_id",
        string="Dados das duplicatas NT 2011/004",
        help=u"Dados das duplicatas NT 2011/004"
    )


class comb(spec_models.AbstractSpecMixin):
    _description = u"Informar apenas para operações com combustíveis líquidos"
    _name = 'nfe.v3_10.comb'
    _generateds_type = 'combType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_cProdANP'

    nfe_cProdANP = fields.Char(
        string="Código de produto da ANP",
        xsd_required=True,
        help=(u"Código de produto da ANP. codificação de produtos do SIMP"
              u"(http://www.anp.gov.br)"))
    nfe_pMixGN = fields.Monetary(
        digits=4, string="Percentual de gas natural para o produto GLP",
        help=u"Percentual de gas natural para o produto GLP")
    nfe_CODIF = fields.Char(
        string="Código de autorização / registro do CODIF",
        help=(u"Código de autorização / registro do CODIF. Informar apenas"
              u"quando a UF utilizar o CODIF (Sistema de Controle do"
              u"Diferimento do Imposto nas Operações com AEAC - Álcool"
              u"Etílico Anidro Combustível)."))
    nfe_qTemp = fields.Monetary(
        digits=4, string="Quantidade de combustível",
        help=(u"Quantidade de combustível"
              u"faturada à temperatura ambiente."
              u"Informar quando a quantidade"
              u"faturada informada no campo"
              u"qCom (I10) tiver sido ajustada para"
              u"uma temperatura diferente da"
              u"ambiente."))
    nfe_UFCons = fields.Selection(
        TUf,
        string="Sigla da UF de Consumo",
        xsd_required=True,
        help=u"Tipo Sigla da UF")
    nfe_CIDE = fields.Many2one(
        "nfe.v3_10.cide",
        string="CIDE Combustíveis",
        help=u"CIDE Combustíveis")
    nfe_encerrante = fields.Many2one(
        "nfe.v3_10.encerrante",
        string="Informações do grupo de encerrante",
        help=u"Informações do grupo de encerrante")


class compra(spec_models.AbstractSpecMixin):
    _description = (u"Informações de compras  (Nota de Empenho, Pedido e"
                    u"Contrato)")
    _name = 'nfe.v3_10.compra'
    _generateds_type = 'compraType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_xNEmp'

    nfe_xNEmp = fields.Char(
        string="Informação da Nota de Empenho de compras públicas",
        help=u"Informação da Nota de Empenho de compras públicas (NT2011/004)")
    nfe_xPed = fields.Char(
        string="Informação do pedido",
        help=u"Informação do pedido")
    nfe_xCont = fields.Char(
        string="Informação do contrato",
        help=u"Informação do contrato")


class deduc(spec_models.AbstractSpecMixin):
    _description = u"Deduções - Taxas e Contribuições"
    _name = 'nfe.v3_10.deduc'
    _generateds_type = 'deducType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_xDed'

    nfe_deduc_cana_id = fields.Many2one(
        "nfe.v3_10.cana")
    nfe_xDed = fields.Char(
        string="Descrição da Dedução", xsd_required=True,
        help=u"Descrição da Dedução")
    nfe_vDed = fields.Monetary(
        digits=2, string="valor da dedução", xsd_required=True,
        help=u"valor da dedução")


class dest(spec_models.AbstractSpecMixin):
    _description = u"Identificação do Destinatário"
    _name = 'nfe.v3_10.dest'
    _generateds_type = 'destType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CNPJ'

    nfe_choice7 = fields.Selection([
        ('nfe_CNPJ', 'CNPJ'),
        ('nfe_CPF', 'CPF'),
        ('nfe_idEstrangeiro', 'idEstrangeiro')],
        "CNPJ/CPF/idEstrangeiro",
        default="nfe_CNPJ")
    nfe_CNPJ = fields.Char(
        choice='7',
        string="Número do CNPJ", xsd_required=True,
        help=u"Número do CNPJ")
    nfe_CPF = fields.Char(
        choice='7',
        string="Número do CPF", xsd_required=True,
        help=u"Número do CPF")
    nfe_idEstrangeiro = fields.Char(
        choice='7',
        string="Identificador do destinatário",
        xsd_required=True,
        help=u"Identificador do destinatário, em caso de comprador estrangeiro")
    nfe_xNome = fields.Char(
        string="Razão Social ou nome do destinatário",
        help=u"Razão Social ou nome do destinatário")
    nfe_enderDest = fields.Many2one(
        "nfe.v3_10.tendereco",
        string="Dados do endereço",
        help=u"Dados do endereço")
    nfe_indIEDest = fields.Selection(
        indIEDestType,
        string="Indicador da IE do destinatário:",
        xsd_required=True,
        help=u"Indicador da IE do destinatário:")
    nfe_IE = fields.Char(
        string="Inscrição Estadual",
        help=(u"Inscrição Estadual (obrigatório nas operações com contribuintes"
              u"do ICMS)"))
    nfe_ISUF = fields.Char(
        string="Inscrição na SUFRAMA",
        help=(u"Inscrição na SUFRAMA (Obrigatório nas operações com as áreas"
              u"com benefícios de incentivos fiscais sob controle da"
              u"SUFRAMA) PL_005d - 11/08/09 - alterado para aceitar 8 ou 9"
              u"dígitos"))
    nfe_IM = fields.Char(
        string="Inscrição Municipal do tomador do serviço",
        help=u"Inscrição Municipal do tomador do serviço")
    nfe_email = fields.Char(
        string="Informar o e",
        help=(u"Informar o e-mail do destinatário. O campo pode ser utilizado"
              u"para informar o e-mail"
              u"de recepção da NF-e indicada pelo destinatário"))


class detExport(spec_models.AbstractSpecMixin):
    _description = u"Detalhe da exportação"
    _name = 'nfe.v3_10.detexport'
    _generateds_type = 'detExportType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_nDraw'

    nfe_detExport_prod_id = fields.Many2one(
        "nfe.v3_10.prod")
    nfe_nDraw = fields.Char(
        string="Número do ato concessório de Drawback",
        help=u"Número do ato concessório de Drawback")
    nfe_exportInd = fields.Many2one(
        "nfe.v3_10.exportind",
        string="Exportação indireta",
        help=u"Exportação indireta")


class det(spec_models.AbstractSpecMixin):
    _description = u"Dados dos detalhes da NF-e"
    _name = 'nfe.v3_10.det'
    _generateds_type = 'detType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_nItem'

    nfe_det_infNFe_id = fields.Many2one(
        "nfe.v3_10.infnfe")
    nfe_nItem = fields.Char(
        string="nItem", xsd_required=True)
    nfe_prod = fields.Many2one(
        "nfe.v3_10.prod",
        string="Dados dos produtos e serviços da NF",
        xsd_required=True,
        help=u"Dados dos produtos e serviços da NF-e")
    nfe_imposto = fields.Many2one(
        "nfe.v3_10.imposto",
        string="Tributos incidentes nos produtos ou serviços da NF",
        xsd_required=True,
        help=u"Tributos incidentes nos produtos ou serviços da NF-e")
    nfe_impostoDevol = fields.Many2one(
        "nfe.v3_10.impostodevol",
        string="impostoDevol")
    nfe_infAdProd = fields.Char(
        string="Informações adicionais do produto",
        help=(u"Informações adicionais do produto (norma referenciada,"
              u"informações complementares, etc)"))


class dup(spec_models.AbstractSpecMixin):
    _description = u"Dados das duplicatas NT 2011/004"
    _name = 'nfe.v3_10.dup'
    _generateds_type = 'dupType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_nDup'

    nfe_dup_cobr_id = fields.Many2one(
        "nfe.v3_10.cobr")
    nfe_nDup = fields.Char(
        string="Número da duplicata",
        help=u"Número da duplicata")
    nfe_dVenc = fields.Char(
        string="Data de vencimento da duplicata",
        help=u"Data de vencimento da duplicata (AAAA-MM-DD)")
    nfe_vDup = fields.Monetary(
        digits=2, string="Valor da duplicata", xsd_required=True,
        help=u"Valor da duplicata")


class emit(spec_models.AbstractSpecMixin):
    _description = u"Identificação do emitente"
    _name = 'nfe.v3_10.emit'
    _generateds_type = 'emitType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CNPJ'

    nfe_choice6 = fields.Selection([
        ('nfe_CNPJ', 'CNPJ'),
        ('nfe_CPF', 'CPF')],
        "CNPJ/CPF",
        default="nfe_CNPJ")
    nfe_CNPJ = fields.Char(
        choice='6',
        string="Número do CNPJ do emitente",
        xsd_required=True,
        help=u"Número do CNPJ do emitente")
    nfe_CPF = fields.Char(
        choice='6',
        string="Número do CPF do emitente",
        xsd_required=True,
        help=u"Número do CPF do emitente")
    nfe_xNome = fields.Char(
        string="Razão Social ou Nome do emitente",
        xsd_required=True,
        help=u"Razão Social ou Nome do emitente")
    nfe_xFant = fields.Char(
        string="Nome fantasia",
        help=u"Nome fantasia")
    nfe_enderEmit = fields.Many2one(
        "nfe.v3_10.tenderemi",
        string="Endereço do emitente",
        xsd_required=True,
        help=u"Endereço do emitente")
    nfe_IE = fields.Char(
        string="Inscrição Estadual do Emitente",
        xsd_required=True,
        help=u"Inscrição Estadual do Emitente")
    nfe_IEST = fields.Char(
        string="Inscricao Estadual do Substituto Tributário",
        help=u"Inscricao Estadual do Substituto Tributário")
    nfe_IM = fields.Char(
        string="Inscrição Municipal",
        help=u"Inscrição Municipal")
    nfe_CNAE = fields.Char(
        string="CNAE Fiscal",
        help=u"CNAE Fiscal")
    nfe_CRT = fields.Selection(
        CRTType,
        string="Código de Regime Tributário. ",
        xsd_required=True,
        help=(u"Código de Regime Tributário."
              u"Este campo será obrigatoriamente preenchido com:"))


class encerrante(spec_models.AbstractSpecMixin):
    _description = u"Informações do grupo de 'encerrante'"
    _name = 'nfe.v3_10.encerrante'
    _generateds_type = 'encerranteType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_nBico'

    nfe_nBico = fields.Char(
        string="Numero de identificação do Bico utilizado no abastecimento",
        xsd_required=True,
        help=u"Numero de identificação do Bico utilizado no abastecimento")
    nfe_nBomba = fields.Char(
        string="nBomba",
        help=(u"Numero de identificação da bomba ao qual o bico está"
              u"interligado"))
    nfe_nTanque = fields.Char(
        string="nTanque", xsd_required=True,
        help=(u"Numero de identificação do tanque ao qual o bico está"
              u"interligado"))
    nfe_vEncIni = fields.Monetary(
        digits=3, string="Valor do Encerrante no ínicio do abastecimento",
        xsd_required=True,
        help=u"Valor do Encerrante no ínicio do abastecimento")
    nfe_vEncFin = fields.Monetary(
        digits=3, string="Valor do Encerrante no final do abastecimento",
        xsd_required=True,
        help=u"Valor do Encerrante no final do abastecimento")


class exportInd(spec_models.AbstractSpecMixin):
    _description = u"Exportação indireta"
    _name = 'nfe.v3_10.exportind'
    _generateds_type = 'exportIndType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_nRE'

    nfe_nRE = fields.Char(
        string="Registro de exportação", xsd_required=True,
        help=u"Registro de exportação")
    nfe_chNFe = fields.Char(
        string="Chave de acesso da NF", xsd_required=True,
        help=u"Chave de acesso da NF-e recebida para exportação")
    nfe_qExport = fields.Monetary(
        digits=4, string="Quantidade do item efetivamente exportado",
        xsd_required=True,
        help=u"Quantidade do item efetivamente exportado")


class exporta(spec_models.AbstractSpecMixin):
    _description = u"Informações de exportação"
    _name = 'nfe.v3_10.exporta'
    _generateds_type = 'exportaType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_UFSaidaPais'

    nfe_UFSaidaPais = fields.Selection(
        TUfEmi,
        string="Sigla da UF de Embarque ou de transposição de fronteira",
        xsd_required=True,
        help=u"Tipo Sigla da UF de emissor // acrescentado em 24/10/08")
    nfe_xLocExporta = fields.Char(
        string="Local de Embarque ou de transposição de fronteira",
        xsd_required=True,
        help=u"Local de Embarque ou de transposição de fronteira")
    nfe_xLocDespacho = fields.Char(
        string="Descrição do local de despacho",
        help=u"Descrição do local de despacho")


class fat(spec_models.AbstractSpecMixin):
    _description = u"Dados da fatura"
    _name = 'nfe.v3_10.fat'
    _generateds_type = 'fatType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_nFat'

    nfe_nFat = fields.Char(
        string="Número da fatura",
        help=u"Número da fatura")
    nfe_vOrig = fields.Monetary(
        digits=2, string="Valor original da fatura",
        help=u"Valor original da fatura")
    nfe_vDesc = fields.Monetary(
        digits=2, string="Valor do desconto da fatura",
        help=u"Valor do desconto da fatura")
    nfe_vLiq = fields.Monetary(
        digits=2, string="Valor líquido da fatura",
        help=u"Valor líquido da fatura")


class forDia(spec_models.AbstractSpecMixin):
    _description = u"Fornecimentos diários"
    _name = 'nfe.v3_10.fordia'
    _generateds_type = 'forDiaType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_dia'

    nfe_forDia_cana_id = fields.Many2one(
        "nfe.v3_10.cana")
    nfe_dia = fields.Char(
        string="dia", xsd_required=True)
    nfe_qtde = fields.Monetary(
        digits=0, string="Quantidade em quilogramas",
        xsd_required=True,
        help=u"Quantidade em quilogramas - peso líquido")


class ide(spec_models.AbstractSpecMixin):
    _description = u"identificação da NF-e"
    _name = 'nfe.v3_10.ide'
    _generateds_type = 'ideType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_cUF'

    nfe_cUF = fields.Selection(
        TCodUfIBGE,
        string="Código da UF do emitente do Documento Fiscal",
        xsd_required=True,
        help=u"Tipo Código da UF da tabela do IBGE")
    nfe_cNF = fields.Char(
        string="Código numérico que compõe a Chave de Acesso",
        xsd_required=True,
        help=(u"Código numérico que compõe a Chave de Acesso. Número aleatório"
              u"gerado pelo emitente para cada NF-e."))
    nfe_natOp = fields.Char(
        string="Descrição da Natureza da Operação",
        xsd_required=True,
        help=u"Descrição da Natureza da Operação")
    nfe_indPag = fields.Selection(
        indPagType,
        string="Indicador da forma de pagamento:",
        xsd_required=True,
        help=u"Indicador da forma de pagamento:")
    nfe_mod = fields.Selection(
        TMod,
        string="Código do modelo do Documento Fiscal",
        xsd_required=True,
        help=u"Tipo Modelo Documento Fiscal")
    nfe_serie = fields.Char(
        string="Série do Documento Fiscal",
        xsd_required=True,
        help=(u"Série do Documento Fiscal"
              u"série normal 0-889"
              u"Avulsa Fisco 890-899"
              u"SCAN 900-999"))
    nfe_nNF = fields.Char(
        string="Número do Documento Fiscal",
        xsd_required=True,
        help=u"Número do Documento Fiscal")
    nfe_dhEmi = fields.Char(
        string="Data e Hora de emissão do Documento Fiscal",
        xsd_required=True,
        help=(u"Data e Hora de emissão do Documento Fiscal (AAAA-MM-"
              u"DDThh:mm:ssTZD) ex.: 2012-09-01T13:00:00-03:00"))
    nfe_dhSaiEnt = fields.Char(
        string="Data e Hora da saída ou de entrada da mercadoria / produto",
        help=(u"Data e Hora da saída ou de entrada da mercadoria / produto"
              u"(AAAA-MM-DDTHH:mm:ssTZD)"))
    nfe_tpNF = fields.Selection(
        tpNFType,
        string="Tipo do Documento Fiscal (0",
        xsd_required=True,
        help=u"Tipo do Documento Fiscal (0 - entrada; 1 - saída)")
    nfe_idDest = fields.Selection(
        idDestType,
        string="Identificador de Local de destino da operação",
        xsd_required=True,
        help=(u"Identificador de Local de destino da operação"
              u"(1-Interna;2-Interestadual;3-Exterior)"))
    nfe_cMunFG = fields.Char(
        string="Código do Município de Ocorrência do Fato Gerador",
        xsd_required=True,
        help=(u"Código do Município de Ocorrência do Fato Gerador (utilizar a"
              u"tabela do IBGE)"))
    nfe_tpImp = fields.Selection(
        tpImpType,
        string="Formato de impressão do DANFE (0",
        xsd_required=True,
        help=(u"Formato de impressão do DANFE (0-sem DANFE;1-DANFe Retrato;"
              u"2-DANFe Paisagem;3-DANFe Simplificado;"
              u"4-DANFe NFC-e;5-DANFe NFC-e em mensagem eletrônica)"))
    nfe_tpEmis = fields.Selection(
        tpEmisType,
        string="Forma de emissão da NF-e",
        xsd_required=True,
        help=u"Forma de emissão da NF-e")
    nfe_cDV = fields.Char(
        string="Digito Verificador da Chave de Acesso da NF",
        xsd_required=True,
        help=u"Digito Verificador da Chave de Acesso da NF-e")
    nfe_tpAmb = fields.Selection(
        TAmb,
        string="Identificação do Ambiente:",
        xsd_required=True,
        help=u"Tipo Ambiente")
    nfe_finNFe = fields.Selection(
        TFinNFe,
        string="Finalidade da emissão da NF-e:",
        xsd_required=True,
        help=(u"Tipo Finalidade da NF-e (1=Normal; 2=Complementar; 3=Ajuste;"
              u"4=Devolução/Retorno)"))
    nfe_indFinal = fields.Selection(
        indFinalType,
        string="Indica operação com consumidor final",
        xsd_required=True,
        help=u"Indica operação com consumidor final (0-Não;1-Consumidor Final)")
    nfe_indPres = fields.Selection(
        indPresType,
        string="indPres", xsd_required=True,
        help=(u"Indicador de presença do comprador no estabelecimento comercial"
              u"no momento da oepração"
              u"(0-Não se aplica (ex."
              u"Nota Fiscal complementar ou de ajuste"
              u"1-Operação presencial"
              u"2-Não presencial, internet"
              u"3-Não presencial, teleatendimento"
              u"4-NFC-e entrega em domicílio"
              u"9-Não presencial, outros)"))
    nfe_procEmi = fields.Selection(
        TProcEmi,
        string="Processo de emissão utilizado com a seguinte codificação:",
        xsd_required=True,
        help=u"Tipo processo de emissão da NF-e")
    nfe_verProc = fields.Char(
        string="versão do aplicativo utilizado no processo de",
        xsd_required=True,
        help=(u"versão do aplicativo utilizado no processo de"
              u"emissão"))
    nfe_dhCont = fields.Char(
        string="dhCont",
        help=(u"Informar a data e hora de entrada em contingência contingência"
              u"no formato  (AAAA-MM-DDThh:mm:ssTZD) ex.:"
              u"2012-09-01T13:00:00-03:00."))
    nfe_xJust = fields.Char(
        string="Informar a Justificativa da entrada",
        help=u"Informar a Justificativa da entrada")
    nfe_NFref = fields.One2many(
        "nfe.v3_10.nfref",
        "nfe_NFref_ide_id",
        string="Grupo de infromações da NF referenciada",
        help=u"Grupo de infromações da NF referenciada"
    )


class impostoDevol(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.impostodevol'
    _generateds_type = 'impostoDevolType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_pDevol'

    nfe_pDevol = fields.Monetary(
        digits=2, string="Percentual de mercadoria devolvida",
        xsd_required=True,
        help=u"Percentual de mercadoria devolvida")
    nfe_IPI = fields.Many2one(
        "nfe.v3_10.ipi",
        string="Informação de IPI devolvido",
        xsd_required=True,
        help=u"Informação de IPI devolvido")


class imposto(spec_models.AbstractSpecMixin):
    _description = u"Tributos incidentes nos produtos ou serviços da NF-e"
    _name = 'nfe.v3_10.imposto'
    _generateds_type = 'impostoType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_vTotTrib'

    nfe_choice10 = fields.Selection([
        ('nfe_ICMS', 'ICMS'),
        ('nfe_II', 'II'),
        ('nfe_IPI', 'IPI'),
        ('nfe_ISSQN', 'ISSQN')],
        "ICMS/II/IPI/ISSQN",
        default="nfe_ICMS")
    nfe_vTotTrib = fields.Monetary(
        digits=2, string="Valor estimado total de impostos federais",
        help=(u"Valor estimado total de impostos federais, estaduais e"
              u"municipais"))
    nfe_ICMS = fields.Many2one(
        "nfe.v3_10.icms",
        choice='10',
        string="Dados do ICMS Normal e ST",
        xsd_required=True,
        help=u"Dados do ICMS Normal e ST")
    nfe_II = fields.Many2one(
        "nfe.v3_10.ii",
        choice='10',
        string="Dados do Imposto de Importação",
        help=u"Dados do Imposto de Importação")
    nfe_IPI = fields.Many2one(
        "nfe.v3_10.tipi",
        choice='10',
        string="IPI")
    nfe_ISSQN = fields.Many2one(
        "nfe.v3_10.issqn",
        choice='10',
        string="ISSQN", xsd_required=True,
        help=u"ISSQN")
    nfe_PIS = fields.Many2one(
        "nfe.v3_10.pis",
        string="Dados do PIS",
        help=u"Dados do PIS")
    nfe_PISST = fields.Many2one(
        "nfe.v3_10.pisst",
        string="Dados do PIS Substituição Tributária",
        help=u"Dados do PIS Substituição Tributária")
    nfe_COFINS = fields.Many2one(
        "nfe.v3_10.cofins",
        string="Dados do COFINS",
        help=u"Dados do COFINS")
    nfe_COFINSST = fields.Many2one(
        "nfe.v3_10.cofinsst",
        string="Dados do COFINS da",
        help=(u"Dados do COFINS da"
              u"Substituição Tributaria;"))
    nfe_ICMSUFDest = fields.Many2one(
        "nfe.v3_10.icmsufdest",
        string="ICMSUFDest",
        help=(u"Grupo a ser informado nas vendas interestarduais para"
              u"consumidor final, não contribuinte de ICMS"))


class infAdic(spec_models.AbstractSpecMixin):
    _description = u"Informações adicionais da NF-e"
    _name = 'nfe.v3_10.infadic'
    _generateds_type = 'infAdicType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_infAdFisco'

    nfe_infAdFisco = fields.Char(
        string="Informações adicionais de interesse do Fisco",
        help=u"Informações adicionais de interesse do Fisco (v2.0)")
    nfe_infCpl = fields.Char(
        string="Informações complementares de interesse do Contribuinte",
        help=u"Informações complementares de interesse do Contribuinte")
    nfe_obsCont = fields.One2many(
        "nfe.v3_10.obscont",
        "nfe_obsCont_infAdic_id",
        string="Campo de uso livre do contribuinte",
        help=(u"Campo de uso livre do contribuinte"
              u"informar o nome do campo no atributo xCampo"
              u"e o conteúdo do campo no xTexto")
    )
    nfe_obsFisco = fields.One2many(
        "nfe.v3_10.obsfisco",
        "nfe_obsFisco_infAdic_id",
        string="Campo de uso exclusivo do Fisco",
        help=(u"Campo de uso exclusivo do Fisco"
              u"informar o nome do campo no atributo xCampo"
              u"e o conteúdo do campo no xTexto")
    )
    nfe_procRef = fields.One2many(
        "nfe.v3_10.procref",
        "nfe_procRef_infAdic_id",
        string="Grupo de informações do  processo referenciado",
        help=u"Grupo de informações do  processo referenciado"
    )


class infNFeSupl(spec_models.AbstractSpecMixin):
    _description = u"Informações suplementares Nota Fiscal"
    _name = 'nfe.v3_10.infnfesupl'
    _generateds_type = 'infNFeSuplType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_qrCode'

    nfe_qrCode = fields.Char(
        string="Texto com o QR", xsd_required=True,
        help=u"Texto com o QR-Code impresso no DANFE NFC-e")


class infNFe(spec_models.AbstractSpecMixin):
    _description = u"Informações da Nota Fiscal eletrônica"
    _name = 'nfe.v3_10.infnfe'
    _generateds_type = 'infNFeType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_versao'

    nfe_versao = fields.Char(
        string="versao", xsd_required=True)
    nfe_Id = fields.Char(
        string="Id", xsd_required=True)
    nfe_ide = fields.Many2one(
        "nfe.v3_10.ide",
        string="identificação da NF-e", xsd_required=True,
        help=u"identificação da NF-e")
    nfe_emit = fields.Many2one(
        "nfe.v3_10.emit",
        string="Identificação do emitente",
        xsd_required=True,
        help=u"Identificação do emitente")
    nfe_avulsa = fields.Many2one(
        "nfe.v3_10.avulsa",
        string="Emissão de avulsa",
        help=u"Emissão de avulsa, informar os dados do Fisco emitente")
    nfe_dest = fields.Many2one(
        "nfe.v3_10.dest",
        string="Identificação do Destinatário  ",
        help=u"Identificação do Destinatário")
    nfe_retirada = fields.Many2one(
        "nfe.v3_10.tlocal",
        string="Identificação do Local de Retirada",
        help=(u"Identificação do Local de Retirada (informar apenas quando for"
              u"diferente do endereço do remetente)"))
    nfe_entrega = fields.Many2one(
        "nfe.v3_10.tlocal",
        string="Identificação do Local de Entrega",
        help=(u"Identificação do Local de Entrega (informar apenas quando for"
              u"diferente do endereço do destinatário)"))
    nfe_autXML = fields.One2many(
        "nfe.v3_10.autxml",
        "nfe_autXML_infNFe_id",
        string="Pessoas autorizadas para o download do XML da NF",
        help=u"Pessoas autorizadas para o download do XML da NF-e"
    )
    nfe_det = fields.One2many(
        "nfe.v3_10.det",
        "nfe_det_infNFe_id",
        string="Dados dos detalhes da NF-e",
        xsd_required=True,
        help=u"Dados dos detalhes da NF-e"
    )
    nfe_total = fields.Many2one(
        "nfe.v3_10.total",
        string="Dados dos totais da NF-e",
        xsd_required=True,
        help=u"Dados dos totais da NF-e")
    nfe_transp = fields.Many2one(
        "nfe.v3_10.transp",
        string="Dados dos transportes da NF-e",
        xsd_required=True,
        help=u"Dados dos transportes da NF-e")
    nfe_cobr = fields.Many2one(
        "nfe.v3_10.cobr",
        string="Dados da cobrança da NF-e",
        help=u"Dados da cobrança da NF-e")
    nfe_pag = fields.One2many(
        "nfe.v3_10.pag",
        "nfe_pag_infNFe_id",
        string="Dados de Pagamento",
        help=u"Dados de Pagamento. Obrigatório apenas para (NFC-e) NT 2012/004"
    )
    nfe_infAdic = fields.Many2one(
        "nfe.v3_10.infadic",
        string="Informações adicionais da NF-e",
        help=u"Informações adicionais da NF-e")
    nfe_exporta = fields.Many2one(
        "nfe.v3_10.exporta",
        string="Informações de exportação",
        help=u"Informações de exportação")
    nfe_compra = fields.Many2one(
        "nfe.v3_10.compra",
        string="Informações de compras",
        help=u"Informações de compras  (Nota de Empenho, Pedido e Contrato)")
    nfe_cana = fields.Many2one(
        "nfe.v3_10.cana",
        string="Informações de registro aquisições de cana",
        help=u"Informações de registro aquisições de cana")


class infProt(spec_models.AbstractSpecMixin):
    _description = u"Dados do protocolo de status"
    _name = 'nfe.v3_10.infprot'
    _generateds_type = 'infProtType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Id'

    nfe_Id = fields.Char(
        string="Id")
    nfe_tpAmb = fields.Selection(
        TAmb,
        string="Identificação do Ambiente:",
        xsd_required=True,
        help=u"Tipo Ambiente")
    nfe_verAplic = fields.Char(
        string="Versão do Aplicativo que processou a NF",
        xsd_required=True,
        help=u"Versão do Aplicativo que processou a NF-e")
    nfe_chNFe = fields.Char(
        string="Chaves de acesso da NF-e",
        xsd_required=True,
        help=(u"Chaves de acesso da NF-e, compostas por: UF do emitente, AAMM"
              u"da emissão da NFe, CNPJ do emitente, modelo, série e número"
              u"da NF-e e código numérico+DV."))
    nfe_dhRecbto = fields.Char(
        string="Data e hora de processamento",
        xsd_required=True,
        help=(u"Data e hora de processamento, no formato AAAA-MM-"
              u"DDTHH:MM:SSTZD. Deve ser preenchida com data e hora da"
              u"gravação no Banco em caso de Confirmação. Em caso de"
              u"Rejeição, com data e hora do recebimento do Lote de NF-e"
              u"enviado."))
    nfe_nProt = fields.Char(
        string="Número do Protocolo de Status da NF",
        help=(u"Número do Protocolo de Status da NF-e. 1 posição (1 –"
              u"Secretaria de Fazenda Estadual 2 – Receita Federal); 2 -"
              u"códiga da UF - 2 posições ano; 10 seqüencial no ano."))
    nfe_digVal = fields.Char(
        string="Digest Value da NF-e processada",
        help=(u"Digest Value da NF-e processada. Utilizado para conferir a"
              u"integridade da NF-e original."))
    nfe_cStat = fields.Char(
        string="Código do status da mensagem enviada",
        xsd_required=True,
        help=u"Código do status da mensagem enviada.")
    nfe_xMotivo = fields.Char(
        string="Descrição literal do status do serviço solicitado",
        xsd_required=True,
        help=u"Descrição literal do status do serviço solicitado.")


class infRec(spec_models.AbstractSpecMixin):
    _description = u"Dados do Recibo do Lote"
    _name = 'nfe.v3_10.infrec'
    _generateds_type = 'infRecType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_nRec'

    nfe_nRec = fields.Char(
        string="Número do Recibo", xsd_required=True,
        help=u"Número do Recibo")
    nfe_tMed = fields.Char(
        string="Tempo médio de resposta do serviço",
        xsd_required=True,
        help=(u"Tempo médio de resposta do serviço (em segundos) dos últimos 5"
              u"minutos"))


class lacres(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.lacres'
    _generateds_type = 'lacresType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_nLacre'

    nfe_lacres_vol_id = fields.Many2one(
        "nfe.v3_10.vol")
    nfe_nLacre = fields.Char(
        string="Número dos Lacres", xsd_required=True,
        help=u"Número dos Lacres")


class med(spec_models.AbstractSpecMixin):
    _description = (u"grupo do detalhamento de Medicamentos e de matérias-primas"
                    u"farmacêuticas")
    _name = 'nfe.v3_10.med'
    _generateds_type = 'medType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_nLote'

    nfe_med_prod_id = fields.Many2one(
        "nfe.v3_10.prod")
    nfe_nLote = fields.Char(
        string="Número do lote do medicamento",
        xsd_required=True,
        help=u"Número do lote do medicamento")
    nfe_qLote = fields.Monetary(
        digits=3, string="Quantidade de produtos no lote",
        xsd_required=True,
        help=u"Quantidade de produtos no lote")
    nfe_dFab = fields.Char(
        string="Data de Fabricação do medicamento",
        xsd_required=True,
        help=u"Data de Fabricação do medicamento (AAAA-MM-DD)")
    nfe_dVal = fields.Char(
        string="Data de validade do medicamento",
        xsd_required=True,
        help=u"Data de validade do medicamento (AAAA-MM-DD)")
    nfe_vPMC = fields.Monetary(
        digits=2, string="Preço Máximo ao Consumidor",
        xsd_required=True,
        help=u"Preço Máximo ao Consumidor")


class obsCont(spec_models.AbstractSpecMixin):
    _description = (u"Campo de uso livre do contribuinte"
                    u"informar o nome do campo no atributo xCampo"
                    u"e o conteúdo do campo no xTexto")
    _name = 'nfe.v3_10.obscont'
    _generateds_type = 'obsContType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_xCampo'

    nfe_obsCont_infAdic_id = fields.Many2one(
        "nfe.v3_10.infadic")
    nfe_xCampo = fields.Char(
        string="xCampo", xsd_required=True)
    nfe_xTexto = fields.Char(
        string="xTexto", xsd_required=True)


class obsFisco(spec_models.AbstractSpecMixin):
    _description = (u"Campo de uso exclusivo do Fisco"
                    u"informar o nome do campo no atributo xCampo"
                    u"e o conteúdo do campo no xTexto")
    _name = 'nfe.v3_10.obsfisco'
    _generateds_type = 'obsFiscoType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_xCampo'

    nfe_obsFisco_infAdic_id = fields.Many2one(
        "nfe.v3_10.infadic")
    nfe_xCampo = fields.Char(
        string="xCampo", xsd_required=True)
    nfe_xTexto = fields.Char(
        string="xTexto", xsd_required=True)


class pag(spec_models.AbstractSpecMixin):
    _description = (u"Dados de Pagamento. Obrigatório apenas para (NFC-e) NT"
                    u"2012/004")
    _name = 'nfe.v3_10.pag'
    _generateds_type = 'pagType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_tPag'

    nfe_pag_infNFe_id = fields.Many2one(
        "nfe.v3_10.infnfe")
    nfe_tPag = fields.Selection(
        tPagType,
        string="Forma de Pagamento:01", xsd_required=True,
        help=u"Forma de Pagamento")
    nfe_vPag = fields.Monetary(
        digits=2, string="Valor do Pagamento", xsd_required=True,
        help=u"Valor do Pagamento")
    nfe_card = fields.Many2one(
        "nfe.v3_10.card",
        string="Grupo de Cartões",
        help=u"Grupo de Cartões")


class procRef(spec_models.AbstractSpecMixin):
    _description = u"Grupo de informações do  processo referenciado"
    _name = 'nfe.v3_10.procref'
    _generateds_type = 'procRefType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_nProc'

    nfe_procRef_infAdic_id = fields.Many2one(
        "nfe.v3_10.infadic")
    nfe_nProc = fields.Char(
        string="Indentificador do processo ou ato",
        xsd_required=True,
        help=(u"Indentificador do processo ou ato"
              u"concessório"))
    nfe_indProc = fields.Selection(
        indProcType,
        string="Origem do processo", xsd_required=True,
        help=u"Origem do processo, informar com:")


class prod(spec_models.AbstractSpecMixin):
    _description = u"Dados dos produtos e serviços da NF-e"
    _name = 'nfe.v3_10.prod'
    _generateds_type = 'prodType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_cProd'

    nfe_choice9 = fields.Selection([
        ('nfe_veicProd', 'veicProd'),
        ('nfe_med', 'med'),
        ('nfe_arma', 'arma'),
        ('nfe_comb', 'comb'),
        ('nfe_nRECOPI', 'nRECOPI')],
        "veicProd/med/arma/comb/nRECOPI",
        default="nfe_veicProd")
    nfe_cProd = fields.Char(
        string="Código do produto ou serviço",
        xsd_required=True,
        help=(u"Código do produto ou serviço. Preencher com CFOP caso se trate"
              u"de itens não relacionados com mercadorias/produto e que o"
              u"contribuinte não possua codificação própria"
              u"Formato ”CFOP9999”."))
    nfe_cEAN = fields.Char(
        string="GTIN", xsd_required=True,
        help=(u"GTIN (Global Trade Item Number) do produto, antigo código EAN"
              u"ou código de barras"))
    nfe_xProd = fields.Char(
        string="Descrição do produto ou serviço",
        xsd_required=True,
        help=u"Descrição do produto ou serviço")
    nfe_NCM = fields.Char(
        string="Código NCM (8 posições)", xsd_required=True,
        help=(u"Código NCM (8 posições), será permitida a informação do gênero"
              u"(posição do capítulo do NCM) quando a operação não for de"
              u"comércio exterior (importação/exportação) ou o produto não"
              u"seja tributado pelo IPI. Em caso de item de serviço ou item"
              u"que não tenham produto (Ex. transferência de crédito,"
              u"crédito do ativo imobilizado, etc.), informar o código 00"
              u"(zeros) (v2.0)"))
    nfe_NVE = fields.Char(
        string="Nomenclatura de Valor aduaneio e Estatístico",
        help=u"Nomenclatura de Valor aduaneio e Estatístico")
    nfe_CEST = fields.Char(
        string="Codigo especificador da Substuicao Tributaria",
        help=(u"Codigo especificador da Substuicao Tributaria - CEST, que"
              u"identifica a mercadoria sujeita aos regimes de"
              u"substituicao tributária e de antecipação do recolhimento"
              u"do imposto"))
    nfe_EXTIPI = fields.Char(
        string="Código EX TIPI (3 posições)",
        help=u"Código EX TIPI (3 posições)")
    nfe_CFOP = fields.Char(
        string="Cfop", xsd_required=True,
        help=u"Cfop")
    nfe_uCom = fields.Char(
        string="Unidade comercial", xsd_required=True,
        help=u"Unidade comercial")
    nfe_qCom = fields.Monetary(
        digits=4, string="Quantidade Comercial  do produto",
        xsd_required=True,
        help=(u"Quantidade Comercial  do produto, alterado para aceitar de 0 a"
              u"4 casas decimais e 11 inteiros."))
    nfe_vUnCom = fields.Monetary(
        digits=0, string="Valor unitário de comercialização",
        xsd_required=True,
        help=(u"Valor unitário de comercialização  - alterado para aceitar 0 a"
              u"10 casas decimais e 11 inteiros"))
    nfe_vProd = fields.Monetary(
        digits=2, string="Valor bruto do produto ou serviço",
        xsd_required=True,
        help=u"Valor bruto do produto ou serviço.")
    nfe_cEANTrib = fields.Char(
        string="GTIN", xsd_required=True,
        help=(u"GTIN (Global Trade Item Number) da unidade tributável, antigo"
              u"código EAN ou código de barras"))
    nfe_uTrib = fields.Char(
        string="Unidade Tributável", xsd_required=True,
        help=u"Unidade Tributável")
    nfe_qTrib = fields.Monetary(
        digits=4, string="Quantidade Tributável", xsd_required=True,
        help=(u"Quantidade Tributável - alterado para aceitar de 0 a 4 casas"
              u"decimais e 11 inteiros"))
    nfe_vUnTrib = fields.Monetary(
        digits=0, string="Valor unitário de tributação",
        xsd_required=True,
        help=(u"Valor unitário de tributação - - alterado para aceitar 0 a 10"
              u"casas decimais e 11 inteiros"))
    nfe_vFrete = fields.Monetary(
        digits=2, string="Valor Total do Frete",
        help=u"Valor Total do Frete")
    nfe_vSeg = fields.Monetary(
        digits=2, string="Valor Total do Seguro",
        help=u"Valor Total do Seguro")
    nfe_vDesc = fields.Monetary(
        digits=2, string="Valor do Desconto",
        help=u"Valor do Desconto")
    nfe_vOutro = fields.Monetary(
        digits=2, string="Outras despesas acessórias",
        help=u"Outras despesas acessórias")
    nfe_indTot = fields.Selection(
        indTotType,
        string="Este campo deverá ser preenchido com:",
        xsd_required=True,
        help=u"Este campo deverá ser preenchido com:")
    nfe_DI = fields.One2many(
        "nfe.v3_10.di",
        "nfe_DI_prod_id",
        string="Delcaração de Importação",
        help=(u"Delcaração de Importação"
              u"(NT 2011/004)")
    )
    nfe_detExport = fields.One2many(
        "nfe.v3_10.detexport",
        "nfe_detExport_prod_id",
        string="Detalhe da exportação",
        help=u"Detalhe da exportação"
    )
    nfe_xPed = fields.Char(
        string="pedido de compra",
        help=(u"pedido de compra - Informação de interesse do emissor para"
              u"controle do B2B."))
    nfe_nItemPed = fields.Char(
        string="Número do Item do Pedido de Compra",
        help=(u"Número do Item do Pedido de Compra - Identificação do número do"
              u"item do pedido de Compra"))
    nfe_nFCI = fields.Char(
        string="Número de controle da FCI",
        help=u"Número de controle da FCI - Ficha de Conteúdo de Importação.")
    nfe_veicProd = fields.Many2one(
        "nfe.v3_10.veicprod",
        choice='9',
        string="Veículos novos",
        help=u"Veículos novos")
    nfe_med = fields.One2many(
        "nfe.v3_10.med",
        "nfe_med_prod_id",
        choice='9',
        string="grupo do detalhamento de Medicamentos e de matérias",
        help=(u"grupo do detalhamento de Medicamentos e de matérias-primas"
              u"farmacêuticas")
    )
    nfe_arma = fields.One2many(
        "nfe.v3_10.arma",
        "nfe_arma_prod_id",
        choice='9',
        string="Armamentos",
        help=u"Armamentos"
    )
    nfe_comb = fields.Many2one(
        "nfe.v3_10.comb",
        choice='9',
        string="Informar apenas para operações com combustíveis líquidos",
        help=u"Informar apenas para operações com combustíveis líquidos")
    nfe_nRECOPI = fields.Char(
        choice='9',
        string="Número do RECOPI",
        help=u"Número do RECOPI")


class refECF(spec_models.AbstractSpecMixin):
    _description = u"Grupo do Cupom Fiscal vinculado à NF-e"
    _name = 'nfe.v3_10.refecf'
    _generateds_type = 'refECFType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_mod'

    nfe_mod = fields.Selection(
        modType3,
        string="Código do modelo do Documento Fiscal",
        xsd_required=True,
        help=(u"Código do modelo do Documento Fiscal"
              u"Preencher com '2B', quando se tratar de Cupom Fiscal emitido"
              u"por máquina registradora (não ECF), com '2C', quando se"
              u"tratar de Cupom Fiscal PDV, ou '2D', quando se tratar de"
              u"Cupom Fiscal (emitido por ECF)"))
    nfe_nECF = fields.Char(
        string="nECF", xsd_required=True,
        help=(u"Informar o número de ordem seqüencial do ECF que emitiu o Cupom"
              u"Fiscal vinculado à NF-e"))
    nfe_nCOO = fields.Char(
        string="Informar o Número do Contador de Ordem de Operação",
        xsd_required=True,
        help=(u"Informar o Número do Contador de Ordem de Operação - COO"
              u"vinculado à NF-e"))


class refNFP(spec_models.AbstractSpecMixin):
    _description = u"Grupo com as informações NF de produtor referenciada"
    _name = 'nfe.v3_10.refnfp'
    _generateds_type = 'refNFPType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_cUF'

    nfe_choice5 = fields.Selection([
        ('nfe_CNPJ', 'CNPJ'),
        ('nfe_CPF', 'CPF')],
        "CNPJ/CPF",
        default="nfe_CNPJ")
    nfe_cUF = fields.Selection(
        TCodUfIBGE,
        string="cUF", xsd_required=True,
        help=u"Tipo Código da UF da tabela do IBGE")
    nfe_AAMM = fields.Char(
        string="AAMM da emissão da NF de produtor",
        xsd_required=True,
        help=u"AAMM da emissão da NF de produtor")
    nfe_CNPJ = fields.Char(
        choice='5',
        string="CNPJ do emitente da NF de produtor",
        xsd_required=True,
        help=u"CNPJ do emitente da NF de produtor")
    nfe_CPF = fields.Char(
        choice='5',
        string="CPF do emitente da NF de produtor",
        xsd_required=True,
        help=u"CPF do emitente da NF de produtor")
    nfe_IE = fields.Char(
        string="IE do emitente da NF de Produtor",
        xsd_required=True,
        help=u"IE do emitente da NF de Produtor")
    nfe_mod = fields.Selection(
        modType2,
        string="Código do modelo do Documento Fiscal",
        xsd_required=True,
        help=(u"Código do modelo do Documento Fiscal - utilizar 04 para NF de"
              u"produtor  ou 01 para NF Avulsa"))
    nfe_serie = fields.Char(
        string="Série do Documento Fiscal",
        xsd_required=True,
        help=u"Série do Documento Fiscal, informar zero se inexistentesérie")
    nfe_nNF = fields.Char(
        string="Número do Documento Fiscal",
        xsd_required=True,
        help=u"Número do Documento Fiscal - 1 – 999999999")


class refNF(spec_models.AbstractSpecMixin):
    _description = u"Dados da NF modelo 1/1A referenciada"
    _name = 'nfe.v3_10.refnf'
    _generateds_type = 'refNFType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_cUF'

    nfe_cUF = fields.Selection(
        TCodUfIBGE,
        string="Código da UF do emitente do Documento Fiscal",
        xsd_required=True,
        help=u"Tipo Código da UF da tabela do IBGE")
    nfe_AAMM = fields.Char(
        string="AAMM da emissão", xsd_required=True,
        help=u"AAMM da emissão")
    nfe_CNPJ = fields.Char(
        string="CNPJ do emitente do documento fiscal referenciado",
        xsd_required=True,
        help=u"CNPJ do emitente do documento fiscal referenciado")
    nfe_mod = fields.Selection(
        modType,
        string="Código do modelo do Documento Fiscal",
        xsd_required=True,
        help=(u"Código do modelo do Documento Fiscal. Utilizar 01 para NF"
              u"modelo 1/1A"))
    nfe_serie = fields.Char(
        string="Série do Documento Fiscal",
        xsd_required=True,
        help=u"Série do Documento Fiscal, informar zero se inexistente")
    nfe_nNF = fields.Char(
        string="Número do Documento Fiscal",
        xsd_required=True,
        help=u"Número do Documento Fiscal")


class retTransp(spec_models.AbstractSpecMixin):
    _description = u"Dados da retenção  ICMS do Transporte"
    _name = 'nfe.v3_10.rettransp'
    _generateds_type = 'retTranspType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_vServ'

    nfe_vServ = fields.Monetary(
        digits=2, string="Valor do Serviço", xsd_required=True,
        help=u"Valor do Serviço")
    nfe_vBCRet = fields.Monetary(
        digits=2, string="BC da Retenção do ICMS",
        xsd_required=True,
        help=u"BC da Retenção do ICMS")
    nfe_pICMSRet = fields.Monetary(
        digits=2, string="Alíquota da Retenção",
        xsd_required=True,
        help=u"Alíquota da Retenção")
    nfe_vICMSRet = fields.Monetary(
        digits=2, string="Valor do ICMS Retido",
        xsd_required=True,
        help=u"Valor do ICMS Retido")
    nfe_CFOP = fields.Char(
        string="Código Fiscal de Operações e Prestações",
        xsd_required=True,
        help=u"Código Fiscal de Operações e Prestações")
    nfe_cMunFG = fields.Char(
        string="Código do Município de Ocorrência do Fato Gerador",
        xsd_required=True,
        help=(u"Código do Município de Ocorrência do Fato Gerador (utilizar a"
              u"tabela do IBGE)"))


class retTrib(spec_models.AbstractSpecMixin):
    _description = u"Retenção de Tributos Federais"
    _name = 'nfe.v3_10.rettrib'
    _generateds_type = 'retTribType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_vRetPIS'

    nfe_vRetPIS = fields.Monetary(
        digits=2, string="Valor Retido de PIS",
        help=u"Valor Retido de PIS")
    nfe_vRetCOFINS = fields.Monetary(
        digits=2, string="Valor Retido de COFINS",
        help=u"Valor Retido de COFINS")
    nfe_vRetCSLL = fields.Monetary(
        digits=2, string="Valor Retido de CSLL",
        help=u"Valor Retido de CSLL")
    nfe_vBCIRRF = fields.Monetary(
        digits=2, string="Base de Cálculo do IRRF",
        help=u"Base de Cálculo do IRRF")
    nfe_vIRRF = fields.Monetary(
        digits=2, string="Valor Retido de IRRF",
        help=u"Valor Retido de IRRF")
    nfe_vBCRetPrev = fields.Monetary(
        digits=2, string="Base de Cálculo da Retenção da Previdêncica Social",
        help=u"Base de Cálculo da Retenção da Previdêncica Social")
    nfe_vRetPrev = fields.Monetary(
        digits=2, string="Valor da Retenção da Previdêncica Social",
        help=u"Valor da Retenção da Previdêncica Social")


class total(spec_models.AbstractSpecMixin):
    _description = u"Dados dos totais da NF-e"
    _name = 'nfe.v3_10.total'
    _generateds_type = 'totalType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_ICMSTot'

    nfe_ICMSTot = fields.Many2one(
        "nfe.v3_10.icmstot",
        string="Totais referentes ao ICMS",
        xsd_required=True,
        help=u"Totais referentes ao ICMS")
    nfe_ISSQNtot = fields.Many2one(
        "nfe.v3_10.issqntot",
        string="Totais referentes ao ISSQN",
        help=u"Totais referentes ao ISSQN")
    nfe_retTrib = fields.Many2one(
        "nfe.v3_10.rettrib",
        string="Retenção de Tributos Federais",
        help=u"Retenção de Tributos Federais")


class transp(spec_models.AbstractSpecMixin):
    _description = u"Dados dos transportes da NF-e"
    _name = 'nfe.v3_10.transp'
    _generateds_type = 'transpType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_modFrete'

    nfe_choice18 = fields.Selection([
        ('nfe_veicTransp', 'veicTransp'),
        ('nfe_reboque', 'reboque'),
        ('nfe_vagao', 'vagao'),
        ('nfe_balsa', 'balsa')],
        "veicTransp/reboque/vagao/balsa",
        default="nfe_veicTransp")
    nfe_modFrete = fields.Selection(
        modFreteType,
        string="Modalidade do frete",
        xsd_required=True,
        help=u"Modalidade do frete")
    nfe_transporta = fields.Many2one(
        "nfe.v3_10.transporta",
        string="Dados do transportador",
        help=u"Dados do transportador")
    nfe_retTransp = fields.Many2one(
        "nfe.v3_10.rettransp",
        string="Dados da retenção  ICMS do Transporte",
        help=u"Dados da retenção  ICMS do Transporte")
    nfe_veicTransp = fields.Many2one(
        "nfe.v3_10.tveiculo",
        choice='18',
        string="Dados do veículo",
        help=u"Dados do veículo")
    nfe_reboque = fields.One2many(
        "nfe.v3_10.tveiculo",
        "nfe_reboque_transp_id",
        choice='18',
        string="Dados do reboque/Dolly (v2.0)",
        help=u"Dados do reboque/Dolly (v2.0)"
    )
    nfe_vagao = fields.Char(
        choice='18',
        string="Identificação do vagão (v2.0)",
        help=u"Identificação do vagão (v2.0)")
    nfe_balsa = fields.Char(
        choice='18',
        string="Identificação da balsa (v2.0)",
        help=u"Identificação da balsa (v2.0)")
    nfe_vol = fields.One2many(
        "nfe.v3_10.vol",
        "nfe_vol_transp_id",
        string="Dados dos volumes",
        help=u"Dados dos volumes"
    )


class transporta(spec_models.AbstractSpecMixin):
    _description = u"Dados do transportador"
    _name = 'nfe.v3_10.transporta'
    _generateds_type = 'transportaType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_CNPJ'

    nfe_choice19 = fields.Selection([
        ('nfe_CNPJ', 'CNPJ'),
        ('nfe_CPF', 'CPF')],
        "CNPJ/CPF",
        default="nfe_CNPJ")
    nfe_CNPJ = fields.Char(
        choice='19',
        string="CNPJ do transportador",
        help=u"CNPJ do transportador")
    nfe_CPF = fields.Char(
        choice='19',
        string="CPF do transportador",
        help=u"CPF do transportador")
    nfe_xNome = fields.Char(
        string="Razão Social ou nome do transportador",
        help=u"Razão Social ou nome do transportador")
    nfe_IE = fields.Char(
        string="Inscrição Estadual (v2.0)",
        help=u"Inscrição Estadual (v2.0)")
    nfe_xEnder = fields.Char(
        string="Endereço completo",
        help=u"Endereço completo")
    nfe_xMun = fields.Char(
        string="Nome do munícipio",
        help=u"Nome do munícipio")
    nfe_UF = fields.Selection(
        TUf,
        string="Sigla da UF",
        help=u"Tipo Sigla da UF")


class veicProd(spec_models.AbstractSpecMixin):
    _description = u"Veículos novos"
    _name = 'nfe.v3_10.veicprod'
    _generateds_type = 'veicProdType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_tpOp'

    nfe_tpOp = fields.Selection(
        tpOpType,
        string="Tipo da Operação (1", xsd_required=True,
        help=(u"Tipo da Operação (1 - Venda concessionária; 2 - Faturamento"
              u"direto; 3 - Venda direta; 0 - Outros)"))
    nfe_chassi = fields.Char(
        string="Chassi do veículo", xsd_required=True,
        help=u"Chassi do veículo - VIN (código-identificação-veículo)")
    nfe_cCor = fields.Char(
        string="Cor do veículo", xsd_required=True,
        help=u"Cor do veículo (código de cada montadora)")
    nfe_xCor = fields.Char(
        string="Descrição da cor", xsd_required=True,
        help=u"Descrição da cor")
    nfe_pot = fields.Char(
        string="Potência máxima do motor do veículo em cavalo vapor",
        xsd_required=True,
        help=(u"Potência máxima do motor do veículo em cavalo vapor (CV)."
              u"(potência-veículo)"))
    nfe_cilin = fields.Char(
        string="Capacidade voluntária do motor expressa em centímetros cúbicos",
        xsd_required=True,
        help=(u"Capacidade voluntária do motor expressa em centímetros cúbicos"
              u"(CC). (cilindradas)"))
    nfe_pesoL = fields.Char(
        string="Peso líquido", xsd_required=True,
        help=u"Peso líquido")
    nfe_pesoB = fields.Char(
        string="Peso bruto", xsd_required=True,
        help=u"Peso bruto")
    nfe_nSerie = fields.Char(
        string="Serial (série)", xsd_required=True,
        help=u"Serial (série)")
    nfe_tpComb = fields.Char(
        string="Tipo de combustível", xsd_required=True,
        help=(u"Tipo de combustível-Tabela RENAVAM: 01-Álcool; 02-Gasolina;"
              u"03-Diesel; 16-Álcool/Gas.; 17-Gas./Álcool/GNV;"
              u"18-Gasolina/Elétrico"))
    nfe_nMotor = fields.Char(
        string="Número do motor", xsd_required=True,
        help=u"Número do motor")
    nfe_CMT = fields.Char(
        string="CMT", xsd_required=True,
        help=u"CMT-Capacidade Máxima de Tração - em Toneladas 4 casas decimais")
    nfe_dist = fields.Char(
        string="Distância entre eixos", xsd_required=True,
        help=u"Distância entre eixos")
    nfe_anoMod = fields.Char(
        string="Ano Modelo de Fabricação",
        xsd_required=True,
        help=u"Ano Modelo de Fabricação")
    nfe_anoFab = fields.Char(
        string="Ano de Fabricação", xsd_required=True,
        help=u"Ano de Fabricação")
    nfe_tpPint = fields.Char(
        string="Tipo de pintura", xsd_required=True,
        help=u"Tipo de pintura")
    nfe_tpVeic = fields.Char(
        string="Tipo de veículo", xsd_required=True,
        help=u"Tipo de veículo (utilizar tabela RENAVAM)")
    nfe_espVeic = fields.Char(
        string="Espécie de veículo", xsd_required=True,
        help=u"Espécie de veículo (utilizar tabela RENAVAM)")
    nfe_VIN = fields.Selection(
        VINType,
        string="Informa", xsd_required=True,
        help=u"Informa-se o veículo tem VIN (chassi) remarcado.")
    nfe_condVeic = fields.Selection(
        condVeicType,
        string="Condição do veículo (1",
        xsd_required=True,
        help=(u"Condição do veículo (1 - acabado; 2 - inacabado; 3 - semi-"
              u"acabado)"))
    nfe_cMod = fields.Char(
        string="Código Marca Modelo", xsd_required=True,
        help=u"Código Marca Modelo (utilizar tabela RENAVAM)")
    nfe_cCorDENATRAN = fields.Char(
        string="Código da Cor Segundo as regras de pré",
        xsd_required=True,
        help=(u"Código da Cor Segundo as regras de pré-cadastro do DENATRAN: 01"
              u"-AMARELO;02-AZUL;03-BEGE;04-BRANCA;05-CINZA;06-DOURADA;07-G"
              u"RENA"
              u"08-LARANJA;09-MARROM;10-PRATA;11-PRETA;12-ROSA;13-ROXA;14-VERDE"
              u";15-VERMELHA;16-FANTASIA"))
    nfe_lota = fields.Char(
        string="Quantidade máxima de permitida de passageiros sentados",
        xsd_required=True,
        help=(u"Quantidade máxima de permitida de passageiros sentados,"
              u"inclusive motorista."))
    nfe_tpRest = fields.Selection(
        tpRestType,
        string="Restrição", xsd_required=True,
        help=u"Restrição")


class vol(spec_models.AbstractSpecMixin):
    _description = u"Dados dos volumes"
    _name = 'nfe.v3_10.vol'
    _generateds_type = 'volType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_qVol'

    nfe_vol_transp_id = fields.Many2one(
        "nfe.v3_10.transp")
    nfe_qVol = fields.Char(
        string="Quantidade de volumes transportados",
        help=u"Quantidade de volumes transportados")
    nfe_esp = fields.Char(
        string="Espécie dos volumes transportados",
        help=u"Espécie dos volumes transportados")
    nfe_marca = fields.Char(
        string="Marca dos volumes transportados",
        help=u"Marca dos volumes transportados")
    nfe_nVol = fields.Char(
        string="Numeração dos volumes transportados",
        help=u"Numeração dos volumes transportados")
    nfe_pesoL = fields.Monetary(
        digits=3, string="Peso líquido (em kg)",
        help=u"Peso líquido (em kg)")
    nfe_pesoB = fields.Monetary(
        digits=3, string="Peso bruto (em kg)",
        help=u"Peso bruto (em kg)")
    nfe_lacres = fields.One2many(
        "nfe.v3_10.lacres",
        "nfe_lacres_vol_id",
        string="lacres"
    )
