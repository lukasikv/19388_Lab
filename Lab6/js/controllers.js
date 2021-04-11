var portfolioApp = angular.module('portfolioApp',[]);

portfolioApp.controller('GalleryListCtrl', function($scope)
{
    $scope.galleries = 
    [
        { 'title':'Porsche 911',
        'when':'Kwiecień 2021',
        'thumbnailUrl':'img/p1.jpg'
        },
        { 'title':'Porsche 911',
        'when':'Kwiecień 2021',
        'thumbnailUrl':'img/p2.jpg'
        },
        { 'title':'Porsche 911',
        'when':'Kwiecień 2021',
        'thumbnailUrl':'img/p3.jpg'
        },
        { 'title':'Porsche 911',
        'when':'Kwiecień 2021',
        'thumbnailUrl':'img/p4.jpg'
        },
        { 'title':'Porsche 911',
        'when':'Kwiecień 2021',
        'thumbnailUrl':'img/p5.jpg'
        },
        { 'title':'Nissan GTR',
        'when':'Kwiecień 2021',
        'thumbnailUrl':'img/p6.jpg'
        }
    ];
    $scope.galleries.length;
});