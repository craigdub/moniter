function viewPageLoad(url, time) {
    return '<tr><td>' + url + '</td><td id="td-page-load-' + url + '">Retrieving</td></tr>';
}

function getPageLoad(socket, url) {
    socket.emit('page_load', {url: url});
    socket.on('page_load', function (data) {
        console.log(data['load_time']);
        $('#table-page-load > td > #td-page-load-' + data['url']).text(data['load_time']);
    });
}