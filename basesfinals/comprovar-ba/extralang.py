if is_tonic == "sí":
                        sillaba_list = list(sillaba_text)
                        if sillaba_list[idxgrafnucli] in unaccented_vowels:
                            if sillaba_list[idxgrafnucli] == "e":
                                if (j == self.transpart_[i].size() - 1) and (ends_with_any(word, E_OBERTA)==False) and (ends_with_any(word, E_TANCADA)==False):
                                    # for accute words almost always this is the correct accented e
                                    sillaba_list[idxgrafnucli] = "è"  
                                elif (j == self.transpart_[i].size() - 1) and ends_with_any(word, E_OBERTA):
                                    # for accute words almost always this is the correct accented e
                                    sillaba_list[idxgrafnucli] = "è"
                                elif (j == self.transpart_[i].size() - 1) and ends_with_any(word, E_TANCADA):
                                    # for accute words almost always this is the correct accented e
                                    sillaba_list[idxgrafnucli] = "é"    
                                elif (j == self.transpart_[i].size() - 2) and (ends_with_any(word, E_OBERTA)==False) and (ends_with_any(word, E_TANCADA)==False):
                                    # for accute words almost always this is the correct accented e
                                    sillaba_list[idxgrafnucli] = "è"    
                                elif (j == self.transpart_[i].size() - 2) and ends_with_any(word, E_OBERTA):
                                    # for accute words almost always this is the correct accented e
                                    sillaba_list[idxgrafnucli] = "è"
                                elif (j == self.transpart_[i].size() - 2) and ends_with_any(word, E_TANCADA):
                                    # for accute words almost always this is the correct accented e
                                    sillaba_list[idxgrafnucli] = "é"     
                                else:
                                    # proparoxytone
                                    # almost always this is the correct accented e
                                    sillaba_list[idxgrafnucli] = "è"
                            elif sillaba_list[idxgrafnucli] == "o":
                                if (j == self.transpart_[i].size() - 1) and (ends_with_any(word, O_OBERTA)==False) and (ends_with_any(word, O_TANCADA)==False):
                                    # for accute words almost always this is the correct accented e
                                    sillaba_list[idxgrafnucli] = "ó"  
                                elif (j == self.transpart_[i].size() - 1) and ends_with_any(word, O_OBERTA):
                                    # for accute words almost always this is the correct accented e
                                    sillaba_list[idxgrafnucli] = "ò"
                                elif (j == self.transpart_[i].size() - 1) and ends_with_any(word, O_TANCADA):
                                    # for accute words almost always this is the correct accented e
                                    sillaba_list[idxgrafnucli] = "ó"
                                elif (j == self.transpart_[i].size() - 2) and (ends_with_any(word, O_OBERTA)==False) and (ends_with_any(word, O_TANCADA)==False):
                                    # for accute words almost always this is the correct accented e
                                    sillaba_list[idxgrafnucli] = "ò"         
                                elif (j == self.transpart_[i].size() - 2) and ends_with_any(word, O_OBERTA):
                                    # for accute words almost always this is the correct accented e
                                    sillaba_list[idxgrafnucli] = "ò"
                                elif (j == self.transpart_[i].size() - 2) and ends_with_any(word, O_TANCADA):
                                    # for accute words almost always this is the correct accented e
                                    sillaba_list[idxgrafnucli] = "ó"    
                                else:
                                    # proparoxytone
                                    # almost always this is the correct accented o
                                    sillaba_list[idxgrafnucli] = "ò"
                            else:
                                sillaba_list[idxgrafnucli] = accent_changes[sillaba_list[idxgrafnucli]]
                            
                            sillaba_text = "".join(sillaba_list)

                    stressed_word = stressed_word + sillaba_text
            
            original_word = original_word + word
        
        return stressed_word

    def stress_word(self) -> str:
        
        self.motnorm_ = self.normalize_word(self.motorig_)
        
        self.sillaba_accentua_mot()

        self.stressed_word = self.stress_tonic()
        
        return self.stressed_word