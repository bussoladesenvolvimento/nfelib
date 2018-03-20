# -*- coding: utf-8 -*-

#
# Generated Tue Mar 20 01:42:23 2018 by generateDS.py(Akretion's branch).
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
    ("STATUS", u"STATUS"),
]


class TConsStatServ(spec_models.AbstractSpecMixin):
    _description = u"Tipo Pedido de Consulta do Status do Serviço"
    _name = 'nfe.v3_10.tconsstatserv'
    _generateds_type = 'TConsStatServ'
    _concrete_class = None
    _concrete_rec_name = 'nfe_versao'

    nfe_versao = fields.Char(
        string="versao", xsd_required=True)
    nfe_tpAmb = fields.Selection(
        TAmb,
        string="Identificação do Ambiente:",
        xsd_required=True,
        help=u"Tipo Ambiente")
    nfe_cUF = fields.Selection(
        TCodUfIBGE,
        string="Sigla da UF consultada", xsd_required=True,
        help=u"Tipo Código da UF da tabela do IBGE")
    nfe_xServ = fields.Selection(
        xServType,
        string="Serviço Solicitado", xsd_required=True,
        help=u"Serviço Solicitado")


class TRetConsStatServ(spec_models.AbstractSpecMixin):
    _description = u"Tipo Resultado da Consulta do Status do Serviço"
    _name = 'nfe.v3_10.tretconsstatserv'
    _generateds_type = 'TRetConsStatServ'
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
        string="Código da UF responsável pelo serviço",
        xsd_required=True,
        help=u"Tipo Código da UF da tabela do IBGE")
    nfe_dhRecbto = fields.Char(
        string="Data e hora do recebimento da consulta no formato AAAA",
        xsd_required=True,
        help=(u"Data e hora do recebimento da consulta no formato AAAA-MM-"
              u"DDTHH:MM:SSTZD"))
    nfe_tMed = fields.Char(
        string="Tempo médio de resposta do serviço",
        help=(u"Tempo médio de resposta do serviço (em segundos) dos últimos 5"
              u"minutos"))
    nfe_dhRetorno = fields.Char(
        string="AAAA",
        help=(u"AAAA-MM-DDTHH:MM:SSDeve ser preenchida com data e hora"
              u"previstas para o retorno dos serviços prestados."))
    nfe_xObs = fields.Char(
        string="xObs",
        help=(u"Campo observação utilizado para incluir informações ao"
              u"contribuinte"))
