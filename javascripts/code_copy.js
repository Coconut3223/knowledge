var copyButtons = document.querySelectorAll('.copy-button');

copyButtons.forEach(function(button) {
    button.addEventListener('click', function() {
    var codeBlock = button.parentNode.querySelector('pre code');
    var tempTextArea = document.createElement('textarea');
    tempTextArea.value = codeBlock.textContent;
    
    var excludedContent = codeBlock.querySelectorAll('.output');
    excludedContent.forEach(function(content) {
        tempTextArea.value = tempTextArea.value.replace(content.textContent, '');
    });

    document.body.appendChild(tempTextArea);
    tempTextArea.select();
    document.execCommand('copy');
    document.body.removeChild(tempTextArea);

    button.textContent = '已复制';

    setTimeout(function() {
        button.textContent = '复制';
    }, 2000);
    });
});
