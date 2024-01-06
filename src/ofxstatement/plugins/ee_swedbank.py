from typing import Set, List, Iterable, TextIO, Optional

from ofxstatement.plugin import Plugin
from ofxstatement.parser import StatementParser
from ofxstatement.parser import CsvStatementParser
from ofxstatement.statement import Statement, StatementLine
import csv


class EstoniaSwedbankPlugin(Plugin):

    def get_parser(self, filename: str) -> "SwedbankCsvParser":
        return SwedbankCsvParser(open(filename, "rt"))


class SwedbankCsvParser(CsvStatementParser):

    mappings = {"payee": 3, "date": 2, "id": 8, "amount": 5, "memo":4}
    date_format = "%d.%m.%Y"

    def __init__(self, fin: TextIO) -> None:
        super().__init__(fin)

    def split_records(self) -> Iterable[str]:
        return csv.reader(self.fin, delimiter=';')

    def parse_record(self, line: str) -> StatementLine:
        if (line[9]=="AS" or line[9]=="K2" or line[9]=="LS"):
            return None
        if self.cur_record < 3:
            return None

        line[5] = line[5] if line[7]=="K" else "-"+line[5]
        sl = super(SwedbankCsvParser, self).parse_record(line)
        return sl
