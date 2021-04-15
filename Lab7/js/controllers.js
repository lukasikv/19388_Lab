var portfolioApp = angular.module('portfolioApp',[]);

portfolioApp.controller('GalleryListCtrl', function($scope)
{
    $scope.galleries = 
    [
        { 'title':'Porsche 911',
        'when':'Kwiecień 1999',
        'thumbnailUrl':'img/p1.jpg'
        },
        { 'title':'Porsche 911',
        'when':'Maj 2011',
        'thumbnailUrl':'img/p2.jpg'
        },
        { 'title':'Porsche 911',
        'when':'Czerwiec 2012',
        'thumbnailUrl':'img/p3.jpg'
        },
        { 'title':'Porsche 911',
        'when':'Lipiec 2021',
        'thumbnailUrl':'img/p4.jpg'
        },
        { 'title':'Porsche 911',
        'when':'Kwiecień 2015',
        'thumbnailUrl':'img/p5.jpg'
        },
        { 'title':'Nissan GTR',
        'when':'Kwiecień 2016',
        'thumbnailUrl':'img/p6.jpg'
        }
    ];
    $scope.galleries.length;
    $scope.sortList = 
    [
        {
            'label':'Alfabetycznie',
            'value':'title'
        },
        {
            'label':'Chronologicznie',
            'value':'when'
        },
        {
            'label':'Od Najnowszych',
            'value':'-when'
        },
    ];
});