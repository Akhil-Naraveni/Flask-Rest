class book{
    constructor(bookList){
        this.bookList = bookList
        this.issuedbooks = {}
        
    }
    getBooks(){
        this.bookList.forEach(element => {
            console.log(element)
        });
    }
    issuebook(bookName, user){
        if(this.issuedbooks[bookName] == undefined){
            this.issuedbooks[bookName] = user
        }else{
            console.log("Book has been issued by  others")
        }

    }
    retrunBook(bookName){
        delete this.issuedbooks[bookName]
    }
}
let k = new book("popoopo","vvggv","hgfgc")
console.log(k.issuebook("ram","harry"))
console.log(k.issuedbooks)
console.log(k.issuebook("ram", "hhh"))
console.log(k.issuedbooks)
console.log(k.retrunBook("ram"))
console.log(k.issuebook("ram", "hhh"))