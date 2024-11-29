KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = kapasiteetti or KAPASITEETTI
        self.kasvatuskoko = kasvatuskoko or OLETUSKASVATUS

        if self.kapasiteetti < 0 or self.kasvatuskoko < 0:
            raise ValueError("Kapasiteetti tai kasvatuskoko eivät voi olla negatiivisia")

        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, n):
        if self.kuuluu(n):
            return False

        if self.alkioiden_lkm == len(self.ljono):
            self._laajenna_lista()

        self.ljono[self.alkioiden_lkm] = n
        self.alkioiden_lkm += 1
        return True

    def _laajenna_lista(self):
        uusi_koko = len(self.ljono) + self.kasvatuskoko
        uusi_ljono = self._luo_lista(uusi_koko)
        self._kopioi_lista(self.ljono, uusi_ljono)
        self.ljono = uusi_ljono

    def poista(self, n):
        if not self.kuuluu(n):
            return False

        indeksi = self.ljono.index(n)
        self._siirra_vasemmalle(indeksi)
        self.alkioiden_lkm -= 1
        return True

    def _siirra_vasemmalle(self, indeksi):
        for i in range(indeksi, self.alkioiden_lkm - 1):
            self.ljono[i] = self.ljono[i + 1]
        self.ljono[self.alkioiden_lkm - 1] = 0

    def _kopioi_lista(self, alkuperainen, kohde):
        for i in range(len(alkuperainen)):
            kohde[i] = alkuperainen[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        tulos = IntJoukko()
        for n in a.to_int_list() + b.to_int_list():
            tulos.lisaa(n)
        return tulos

    @staticmethod
    def leikkaus(a, b):
        tulos = IntJoukko()
        b_lista = b.to_int_list()
        for n in a.to_int_list():
            if n in b_lista:
                tulos.lisaa(n)
        return tulos

    @staticmethod
    def erotus(a, b):
        tulos = IntJoukko()
        b_lista = b.to_int_list()
        for n in a.to_int_list():
            if n not in b_lista:
                tulos.lisaa(n)
        return tulos

    def __str__(self):
        return "{" + ", ".join(map(str, self.ljono[:self.alkioiden_lkm])) + "}"
