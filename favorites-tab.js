const favoritesLink=document.querySelector('a[href="#favorites"]');
if(favoritesLink)favoritesLink.addEventListener('click',e=>{e.preventDefault();document.body.classList.add('favorites-open');});
const favoritesPanel=document.querySelector('#favorites');
if(favoritesPanel)favoritesPanel.addEventListener('click',e=>{if(e.target===favoritesPanel)document.body.classList.remove('favorites-open');});
