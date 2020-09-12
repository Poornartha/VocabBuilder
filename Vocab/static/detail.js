
document.getElementbyId('users-btn').addEventListener('click', (event) => {
    document.getElementbyId('users').style.display = 'inline';
    document.getElementbyId('word-wall').style.display = 'None';
});
document.getElementbyId('wordwall-btn').addEventListener('click', (event) => {
    document.getElementbyId('word-wall').style.display = 'inline';
    document.getElementbyId('users').style.display = 'None';
});
