class AuthorData {
    constructor() {
        this.getDataList()
        this.nextORprev()
        this.page = 1
    }
    getDataList(){
        this.data = `https://picsum.photos/v2/list?page=${this.page}&limit=1`
        console.log(this.data);
    }
    async getProfile(){
        this.getDataList()
        let response = await fetch(this.data)
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`)
        }
        return await response.json()
    }
    showProfile(obj){
        let foto = document.getElementById("authorImage")
        let author = document.getElementById("author")
        author.innerHTML = obj[0].author
        foto.src = obj[0].download_url
    }
    nextORprev() {
        let btnPrev = document.getElementById('prev')
        let btnNext = document.getElementById('next')
        btnPrev.addEventListener('click', () => {
            this.page--
            this.getProfile().then(data => {
                this.showProfile(data)
                btnNext.disabled = false
                if (this.page <= 1) {
                    this.page = 1
                    btnPrev.disabled = true
                }
            }).catch(e => console.log(e))
        })
        btnNext.addEventListener('click', () => {
            this.page++
            this.getProfile().then(data => {
                this.showProfile(data)
                btnPrev.disabled = false
                if (this.page >= 993) {
                    this.page = 993
                    btnNext.disabled = true
                }
            }).catch(e => console.log(e))
        })
    }
}
export default AuthorData;