# -*- coding: utf-8 -*-

#
# Generated Tue Mar 20 01:42:21 2018 by generateDS.py(Akretion's branch).
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

# u"Tipo Versão do Leiaute da Cosulta situação NF-e - 3.10"
TVerConsSitNFe = [
    ("3.10", u"3.10"),
]

# u"Serviço Solicitado"
xServType = [
    ("CONSULTAR", u"CONSULTAR"),
]


class TConsSitNFe(spec_models.AbstractSpecMixin):
    _description = (u"Tipo Pedido de Consulta da Situação Atual da Nota Fiscal"
                    u"Eletrônica")
    _name = 'nfe.v3_10.tconssitnfe'
    _generateds_type = 'TConsSitNFe'
    _concrete_class = None
    _concrete_rec_name = 'nfe_versao'

    nfe_versao = fields.Char(
        string="versao", xsd_required=True)
    nfe_tpAmb = fields.Selection(
        TAmb,
        string="Identificação do Ambiente:",
        xsd_required=True,
        help=u"Tipo Ambiente")
    nfe_xServ = fields.Selection(
        xServType,
        string="Serviço Solicitado", xsd_required=True,
        help=u"Serviço Solicitado")
    nfe_chNFe = fields.Char(
        string="Chaves de acesso da NF-e",
        xsd_required=True,
        help=(u"Chaves de acesso da NF-e, compostas por: UF do emitente, AAMM"
              u"da emissão da NFe, CNPJ do emitente, modelo, série e número"
              u"da NF-e e código numérico + DV."))


class TEvento(spec_models.AbstractSpecMixin):
    _description = u"Tipo Evento"
    _name = 'nfe.v3_10.tevento'
    _generateds_type = 'TEvento'
    _concrete_class = None
    _concrete_rec_name = 'nfe_versao'

    nfe_infEvento = fields.Many2one(
        "nfe.v3_10.infevento",
        string="infEvento", xsd_required=True)
    nfe_Signature = fields.Char(
        string="Signature", xsd_required=True)


class TProcEvento(spec_models.AbstractSpecMixin):
    _description = u"Tipo procEvento"
    _name = 'nfe.v3_10.tprocevento'
    _generateds_type = 'TProcEvento'
    _concrete_class = None
    _concrete_rec_name = 'nfe_versao'

    nfe_procEventoNFe_TRetConsSitNFe_id = fields.Many2one(
        "nfe.v3_10.tretconssitnfe")
    nfe_evento = fields.Many2one(
        "nfe.v3_10.tevento",
        string="evento", xsd_required=True)
    nfe_retEvento = fields.Many2one(
        "nfe.v3_10.tretevento",
        string="retEvento", xsd_required=True)


class TProtNFe(spec_models.AbstractSpecMixin):
    _description = (u"Tipo Protocolo de status resultado do processamento da"
                    u"NF-e")
    _name = 'nfe.v3_10.tprotnfe'
    _generateds_type = 'TProtNFe'
    _concrete_class = None
    _concrete_rec_name = 'nfe_versao'

    nfe_infProt = fields.Many2one(
        "nfe.v3_10.infprot",
        string="Dados do protocolo de status",
        xsd_required=True,
        help=u"Dados do protocolo de status")
    nfe_Signature = fields.Char(
        string="Signature")


class TRetCancNFe(spec_models.AbstractSpecMixin):
    _description = (u"Tipo retorno Pedido de Cancelamento da Nota Fiscal"
                    u"Eletrônica")
    _name = 'nfe.v3_10.tretcancnfe'
    _generateds_type = 'TRetCancNFe'
    _concrete_class = None
    _concrete_rec_name = 'nfe_versao'

    nfe_infCanc = fields.Many2one(
        "nfe.v3_10.infcanc",
        string="infCanc", xsd_required=True,
        help=(u"Dados do Resultado do Pedido de Cancelamento da Nota Fiscal"
              u"Eletrônica"))
    nfe_Signature = fields.Char(
        string="Signature")


class TRetConsSitNFe(spec_models.AbstractSpecMixin):
    _description = (u"Tipo Retorno de Pedido de Consulta da Situação Atual da"
                    u"Nota Fiscal"
                    u"Eletrônica")
    _name = 'nfe.v3_10.tretconssitnfe'
    _generateds_type = 'TRetConsSitNFe'
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
        string="código da UF de atendimento",
        xsd_required=True,
        help=u"Tipo Código da UF da tabela do IBGE")
    nfe_dhRecbto = fields.Char(
        string="AAAA-MM-DDTHH:MM:SSTZD",
        xsd_required=True,
        help=u"AAAA-MM-DDTHH:MM:SSTZD")
    nfe_chNFe = fields.Char(
        string="Chaves de acesso da NF",
        xsd_required=True,
        help=u"Chaves de acesso da NF-e consultada")
    nfe_protNFe = fields.Many2one(
        "nfe.v3_10.tprotnfe",
        string="Protocolo de autorização de uso da NF",
        help=u"Protocolo de autorização de uso da NF-e")
    nfe_retCancNFe = fields.Many2one(
        "nfe.v3_10.tretcancnfe",
        string="Protocolo de homologação de cancelamento de uso da NF",
        help=u"Protocolo de homologação de cancelamento de uso da NF-e")
    nfe_procEventoNFe = fields.One2many(
        "nfe.v3_10.tprocevento",
        "nfe_procEventoNFe_TRetConsSitNFe_id",
        string="Protocolo de registro de evento da NF",
        help=u"Protocolo de registro de evento da NF-e"
    )


class TRetEvento(spec_models.AbstractSpecMixin):
    _description = u"Tipo retorno do Evento"
    _name = 'nfe.v3_10.tretevento'
    _generateds_type = 'TRetEvento'
    _concrete_class = None
    _concrete_rec_name = 'nfe_versao'

    nfe_infEvento = fields.Many2one(
        "nfe.v3_10.infevento1",
        string="infEvento", xsd_required=True)
    nfe_Signature = fields.Char(
        string="Signature")


class detEvento(spec_models.AbstractSpecMixin):
    _description = u"Detalhe Específico do Evento"
    _name = 'nfe.v3_10.detevento'
    _generateds_type = 'detEventoType'
    _concrete_class = None
    _concrete_rec_name = 'nfe___ANY__'

    nfe___ANY__ = fields.Char(
        string="__ANY__", xsd_required=True)


class infCanc(spec_models.AbstractSpecMixin):
    _description = (u"Dados do Resultado do Pedido de Cancelamento da Nota"
                    u"Fiscal Eletrônica")
    _name = 'nfe.v3_10.infcanc'
    _generateds_type = 'infCancType'
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
        string="Versão do Aplicativo que processou o pedido de cancelamento",
        xsd_required=True,
        help=u"Versão do Aplicativo que processou o pedido de cancelamento")
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
    nfe_chNFe = fields.Char(
        string="Chaves de acesso da NF-e",
        help=(u"Chaves de acesso da NF-e, compostas por: UF do emitente, AAMM"
              u"da emissão da NFe, CNPJ do emitente, modelo, série e número"
              u"da NF-e e código numérico + DV."))
    nfe_dhRecbto = fields.Datetime(
        string="Data e hora de recebimento",
        help=(u"Data e hora de recebimento, no formato AAAA-MM-DDTHH:MM:SS."
              u"Deve ser preenchida com data e hora da gravação no Banco em"
              u"caso de Confirmação."))
    nfe_nProt = fields.Char(
        string="Número do Protocolo de Status da NF",
        help=(u"Número do Protocolo de Status da NF-e. 1 posição (1 –"
              u"Secretaria de Fazenda Estadual 2 – Receita Federal); 2 -"
              u"código da UF - 2 posições ano; 10 seqüencial no ano."))


class infEvento(spec_models.AbstractSpecMixin):
    _name = 'nfe.v3_10.infevento'
    _generateds_type = 'infEventoType'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Id'

    nfe_choice1 = fields.Selection([
        ('nfe_CNPJ', 'CNPJ'),
        ('nfe_CPF', 'CPF')],
        "CNPJ/CPF",
        default="nfe_CNPJ")
    nfe_Id = fields.Char(
        string="Id", xsd_required=True)
    nfe_cOrgao = fields.Selection(
        TCOrgaoIBGE,
        string="Código do órgão de recepção do Evento",
        xsd_required=True,
        help=u"Tipo Código de orgão (UF da tabela do IBGE + 90 RFB)")
    nfe_tpAmb = fields.Selection(
        TAmb,
        string="Identificação do Ambiente:",
        xsd_required=True,
        help=u"Tipo Ambiente")
    nfe_CNPJ = fields.Char(
        choice='1',
        string="CNPJ", xsd_required=True,
        help=u"CNPJ")
    nfe_CPF = fields.Char(
        choice='1',
        string="CPF", xsd_required=True,
        help=u"CPF")
    nfe_chNFe = fields.Char(
        string="Chave de Acesso da NF", xsd_required=True,
        help=u"Chave de Acesso da NF-e vinculada ao evento")
    nfe_dhEvento = fields.Char(
        string="Data e Hora do Evento",
        xsd_required=True,
        help=(u"Data e Hora do Evento, formato UTC (AAAA-MM-DDThh:mm:ssTZD,"
              u"onde TZD = +hh:mm ou -hh:mm)"))
    nfe_tpEvento = fields.Char(
        string="Tipo do Evento", xsd_required=True,
        help=u"Tipo do Evento")
    nfe_nSeqEvento = fields.Char(
        string="Seqüencial do evento para o mesmo tipo de evento",
        xsd_required=True,
        help=(u"Seqüencial do evento para o mesmo tipo de evento.  Para maioria"
              u"dos eventos será 1, nos casos em que possa existir mais de"
              u"um evento, como é o caso da carta de correção, o autor do"
              u"evento deve numerar de forma seqüencial."))
    nfe_verEvento = fields.Char(
        string="Versão do Tipo do Evento",
        xsd_required=True,
        help=u"Versão do Tipo do Evento")
    nfe_detEvento = fields.Many2one(
        "nfe.v3_10.detevento",
        string="Detalhe Específico do Evento",
        xsd_required=True,
        help=u"Detalhe Específico do Evento")


class infEvento1(spec_models.AbstractSpecMixin):
    _description = u"Identificação do  destinatpario da NF-e"
    _name = 'nfe.v3_10.infevento1'
    _generateds_type = 'infEventoType1'
    _concrete_class = None
    _concrete_rec_name = 'nfe_Id'

    nfe_choice2 = fields.Selection([
        ('nfe_CNPJDest', 'CNPJDest'),
        ('nfe_CPFDest', 'CPFDest')],
        "CNPJDest/CPFDest",
        default="nfe_CNPJDest")
    nfe_Id = fields.Char(
        string="Id")
    nfe_tpAmb = fields.Selection(
        TAmb,
        string="Identificação do Ambiente:",
        xsd_required=True,
        help=u"Tipo Ambiente")
    nfe_verAplic = fields.Char(
        string="Versão do Aplicativo que recebeu o Evento",
        xsd_required=True,
        help=u"Versão do Aplicativo que recebeu o Evento")
    nfe_cOrgao = fields.Selection(
        TCOrgaoIBGE,
        string="Código do órgão de recepção do Evento",
        xsd_required=True,
        help=u"Tipo Código de orgão (UF da tabela do IBGE + 90 RFB)")
    nfe_cStat = fields.Char(
        string="Código do status da registro do Evento",
        xsd_required=True,
        help=u"Código do status da registro do Evento")
    nfe_xMotivo = fields.Char(
        string="Descrição literal do status do registro do Evento",
        xsd_required=True,
        help=u"Descrição literal do status do registro do Evento")
    nfe_chNFe = fields.Char(
        string="Chave de Acesso NF-e vinculada",
        help=u"Chave de Acesso NF-e vinculada")
    nfe_tpEvento = fields.Char(
        string="Tipo do Evento vinculado",
        help=u"Tipo do Evento vinculado")
    nfe_xEvento = fields.Char(
        string="Descrição do Evento",
        help=u"Descrição do Evento")
    nfe_nSeqEvento = fields.Char(
        string="Seqüencial do evento",
        help=u"Seqüencial do evento")
    nfe_CNPJDest = fields.Char(
        choice='2',
        string="CNPJ Destinatário",
        help=u"CNPJ Destinatário")
    nfe_CPFDest = fields.Char(
        choice='2',
        string="CPF Destiantário",
        help=u"CPF Destiantário")
    nfe_emailDest = fields.Char(
        string="email do destinatário",
        help=u"email do destinatário")
    nfe_dhRegEvento = fields.Char(
        string="Data e Hora de registro do evento formato UTC AAAA",
        xsd_required=True,
        help=(u"Data e Hora de registro do evento formato UTC AAAA-MM-"
              u"DDTHH:MM:SSTZD"))
    nfe_nProt = fields.Char(
        string="Número do protocolo de registro do evento",
        help=u"Número do protocolo de registro do evento")


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
    nfe_dhRecbto = fields.Datetime(
        string="Data e hora de processamento",
        xsd_required=True,
        help=(u"Data e hora de processamento, no formato AAAA-MM-DDTHH:MM:SS"
              u"(ou AAAA-MM-DDTHH:MM:SSTZD, de acordo com versão). Deve ser"
              u"preenchida com data e hora da gravação no Banco em caso de"
              u"Confirmação. Em caso de Rejeição, com data e hora do"
              u"recebimento do Lote de NF-e enviado."))
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
