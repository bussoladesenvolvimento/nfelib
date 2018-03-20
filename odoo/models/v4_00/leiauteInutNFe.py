# -*- coding: utf-8 -*-

#
# Generated Tue Mar 20 01:43:10 2018 by generateDS.py(Akretion's branch).
# Python 3.5.2 (default, Sep 14 2017, 22:51:06)  [GCC 5.4.0 20160609]
#
from odoo import fields
from .. import spec_models

# u"Tipo Ambiente"
TAmb = [
    ("1", u"1"),
    ("2", u"2"),
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

# u"Tipo Modelo Documento Fiscal"
TMod = [
    ("55", u"55"),
    ("65", u"65"),
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

# u"Serviço Solicitado"
xServType = [
    ("INUTILIZAR", u"INUTILIZAR"),
]


class TInutNFe(spec_models.AbstractSpecMixin):
    _description = (u"Tipo Pedido de Inutilização de Numeração da Nota Fiscal"
                    u"Eletrônica")
    _name = 'nfe.v3_10.tinutnfe'
    _generateds_type = 'TInutNFe'
    _concrete_class = None
    _concrete_rec_name = 'nfe_versao'

    nfe_versao = fields.Char(
        string="versao", xsd_required=True)
    nfe_infInut = fields.Many2one(
        "nfe.v3_10.infinut",
        string="infInut", xsd_required=True,
        help=(u"Dados do Pedido de Inutilização de Numeração da Nota Fiscal"
              u"Eletrônica"))
    nfe_Signature = fields.Char(
        string="Signature", xsd_required=True)


class TProcInutNFe(spec_models.AbstractSpecMixin):
    _description = (u"Tipo Pedido de inutilzação de númeração de  NF-e"
                    u"processado")
    _name = 'nfe.v3_10.tprocinutnfe'
    _generateds_type = 'TProcInutNFe'
    _concrete_class = None
    _concrete_rec_name = 'nfe_versao'

    nfe_versao = fields.Char(
        string="versao", xsd_required=True)
    nfe_inutNFe = fields.Many2one(
        "nfe.v3_10.tinutnfe",
        string="inutNFe", xsd_required=True)
    nfe_retInutNFe = fields.Many2one(
        "nfe.v3_10.tretinutnfe",
        string="retInutNFe", xsd_required=True)


class TRetInutNFe(spec_models.AbstractSpecMixin):
    _description = (u"Tipo retorno do Pedido de Inutilização de Numeração da"
                    u"Nota Fiscal"
                    u"Eletrônica")
    _name = 'nfe.v3_10.tretinutnfe'
    _generateds_type = 'TRetInutNFe'
    _concrete_class = None
    _concrete_rec_name = 'nfe_versao'

    nfe_versao = fields.Char(
        string="versao", xsd_required=True)
    nfe_infInut = fields.Many2one(
        "nfe.v3_10.infinut1",
        string="infInut", xsd_required=True,
        help=(u"Dados do Retorno do Pedido de Inutilização de Numeração da Nota"
              u"Fiscal Eletrônica"))
    nfe_Signature = fields.Char(
        string="Signature")


class infInut(spec_models.AbstractSpecMixin):
    _description = (u"Dados do Pedido de Inutilização de Numeração da Nota"
                    u"Fiscal Eletrônica")
    _name = 'nfe.v3_10.infinut'
    _generateds_type = 'infInutType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Id'

    nfe_Id = fields.Char(
        string="Id", xsd_required=True)
    nfe_tpAmb = fields.Selection(
        TAmb,
        string="Identificação do Ambiente:",
        xsd_required=True,
        help=u"Tipo Ambiente")
    nfe_xServ = fields.Selection(
        xServType,
        string="Serviço Solicitado", xsd_required=True,
        help=u"Serviço Solicitado")
    nfe_cUF = fields.Selection(
        TCodUfIBGE,
        string="Código da UF do emitente",
        xsd_required=True,
        help=u"Tipo Código da UF da tabela do IBGE")
    nfe_ano = fields.Char(
        string="Ano de inutilização da numeração",
        xsd_required=True,
        help=u"Ano de inutilização da numeração")
    nfe_CNPJ = fields.Char(
        string="CNPJ do emitente", xsd_required=True,
        help=u"CNPJ do emitente")
    nfe_mod = fields.Selection(
        TMod,
        string="Modelo da NF-e (55, 65 etc.)",
        xsd_required=True,
        help=u"Tipo Modelo Documento Fiscal")
    nfe_serie = fields.Char(
        string="Série da NF-e", xsd_required=True,
        help=u"Série da NF-e")
    nfe_nNFIni = fields.Char(
        string="Número da NF-e inicial",
        xsd_required=True,
        help=u"Número da NF-e inicial")
    nfe_nNFFin = fields.Char(
        string="Número da NF-e final", xsd_required=True,
        help=u"Número da NF-e final")
    nfe_xJust = fields.Char(
        string="Justificativa do pedido de inutilização",
        xsd_required=True,
        help=u"Justificativa do pedido de inutilização")


class infInut1(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.infinut1'
    _generateds_type = 'infInutType1'
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
        string="Código da UF que atendeu a solicitação",
        xsd_required=True,
        help=u"Tipo Código da UF da tabela do IBGE")
    nfe_ano = fields.Char(
        string="Ano de inutilização da numeração",
        help=u"Ano de inutilização da numeração")
    nfe_CNPJ = fields.Char(
        string="CNPJ do emitente",
        help=u"CNPJ do emitente")
    nfe_mod = fields.Selection(
        TMod,
        string="Modelo da NF-e (55, etc.)",
        help=u"Tipo Modelo Documento Fiscal")
    nfe_serie = fields.Char(
        string="Série da NF-e",
        help=u"Série da NF-e")
    nfe_nNFIni = fields.Char(
        string="Número da NF-e inicial",
        help=u"Número da NF-e inicial")
    nfe_nNFFin = fields.Char(
        string="Número da NF-e final",
        help=u"Número da NF-e final")
    nfe_dhRecbto = fields.Char(
        string="Data e hora de recebimento",
        xsd_required=True,
        help=(u"Data e hora de recebimento, no formato AAAA-MM-DDTHH:MM:SS."
              u"Deve ser preenchida com data e hora da gravação no Banco em"
              u"caso de Confirmação. Em caso de Rejeição, com data e hora"
              u"do recebimento do Pedido de Inutilização."))
    nfe_nProt = fields.Char(
        string="Número do Protocolo de Status da NF",
        help=(u"Número do Protocolo de Status da NF-e. 1 posição (1 –"
              u"Secretaria de Fazenda Estadual 2 – Receita Federal); 2 -"
              u"código da UF - 2 posições ano; 10 seqüencial no ano."))
