class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq={}
        freq_window={}
        l=0
        formed=0
        

        for i in range(len(t)):
            freq[t[i]]=freq.get(t[i],0)+1
        requried=len(freq)
        res,res_len=[-1,-1],float("infinity")
        for r in range(len(s)):
            freq_window[s[r]]=freq_window.get(s[r],0)+1

            if s[r] in freq and freq_window[s[r]]==freq[s[r]]:
                formed+=1
            while formed == requried:
                if (r-l+1)<res_len:
                    res=(l,r)
                    res_len=r-l+1
                freq_window[s[l]]-=1    
                if s[l] in freq and freq_window[s[l]]< freq[s[l]]:
                    formed-=1
                l+=1
        l,r=res

        return s[l:r+1]


        

        