/*   
Template Name: Color Admin - Responsive Admin Dashboard Template build with Twitter Bootstrap 3.2.0
Version: 1.3.0
Author: Sean Ngu
Website: http://www.seantheme.com/color-admin-v1.3/
    ----------------------------
        APPS CONTENT TABLE
    ----------------------------
    
    <!-- ======== GLOBAL SCRIPT SETTING ======== -->
    01. Handle Scrollbar
    
    02. Handle Sidebar - Menu
    03. Handle Sidebar - Mobile View Toggle
    04. Handle Sidebar - Minify / Expand
    05. Handle Page Load - Fade in
    06. Handle Panel - Remove / Reload / Collapse / Expand
    07. Handle Panel - Draggable
    08. Handle Tooltip & Popover Activation
    09. Handle Scroll to Top Button Activation
    
    <!-- ======== Added in V1.2 ======== -->
    10. Handle Theme & Page Structure Configuration
    11. Handle Theme Panel Expand
	
    <!-- ======== APPLICATION SETTING ======== -->
    Application Controller
*/



/* 01. Handle Scrollbar
------------------------------------------------ */
var handleSlimScroll = function() {
    "use strict";
    $('[data-scrollbar=true]').each( function() {
        generateSlimScroll($(this));
    });
};
var generateSlimScroll = function(element) {
    var dataHeight = $(element).attr('data-height');
        dataHeight = (!dataHeight) ? $(element).height() : dataHeight;
    $(element).slimScroll({height: dataHeight, alwaysVisible: true});
};


/* 02. Handle Sidebar - Menu
------------------------------------------------ */
var handleSidebarMenu = function() {
    "use strict";
    $('.sidebar .nav > .has-sub > a').click(function() {
        var target = $(this).next('.sub-menu');
        var otherMenu = '.sidebar .nav > li.has-sub > .sub-menu';
    
    if ($('.page-sidebar-minified').length === 0) {
        $(otherMenu).not(target).slideUp(250);
        $(target).slideToggle(250);
        }
    });
    $('.sidebar .nav > .has-sub .sub-menu li.has-sub > a').click(function() {
        if ($('.page-sidebar-minified').length === 0) {
            var target = $(this).next('.sub-menu');
            $(target).slideToggle(250);
        }
    });
};


/* 03. Handle Sidebar - Mobile View Toggle
------------------------------------------------ */
var handleMobileSidebarToggle = function() {
    var sidebarProgress = false;
    $('.sidebar').click(function(e) {
        if ($(e.target).closest('.sidebar').length !== 0) {
            sidebarProgress = true;
        } else {
            sidebarProgress = false;
            e.stopPropagation();
        }
    });
    $(document).click(function(e) {
        if ($(e.target).closest('.sidebar').length === 0) {
            sidebarProgress = false;
        }
        if (!e.isPropagationStopped() && sidebarProgress !== true) {
            if ($('#page-container').hasClass('page-sidebar-toggled')) {
                $('#page-container').removeClass('page-sidebar-toggled');
            }
            if ($(window).width() < 979) {
                if ($('#page-container').hasClass('page-with-two-sidebar')) {
                    $('#page-container').removeClass('page-right-sidebar-toggled');
                }
            }
        }
    });
    $('[data-click=right-sidebar-toggled]').click(function(e) {
        e.stopPropagation();
        var targetContainer = '#page-container';
        var targetClass = 'page-right-sidebar-collapsed';
            targetClass = ($(window).width() < 979) ? 'page-right-sidebar-toggled' : targetClass;
        if ($(targetContainer).hasClass(targetClass)) {
            $(targetContainer).removeClass(targetClass);
        } else {
            $(targetContainer).addClass(targetClass);
        }
        if ($(window).width() < 480) {
            $('#page-container').removeClass('page-sidebar-toggled');
        }
    });
    $('[data-click=sidebar-toggled]').click(function(e) {
        e.stopPropagation();
        var sidebarClass = 'page-sidebar-toggled';
        var targetContainer = '#page-container';
        if ($(targetContainer).hasClass(sidebarClass)) {
            $(targetContainer).removeClass(sidebarClass);
        } else {
            $(targetContainer).addClass(sidebarClass);
        }
        if ($(window).width() < 480) {
            $('#page-container').removeClass('page-right-sidebar-toggled');
        }
    });
};


/* 04. Handle Sidebar - Minify / Expand
------------------------------------------------ */
var handleSidebarMinify = function() {
    $('[data-click=sidebar-minify]').click(function(e) {
        e.preventDefault();
        var sidebarClass = 'page-sidebar-minified';
        var targetContainer = '#page-container';
        if ($(targetContainer).hasClass(sidebarClass)) {
            $(targetContainer).removeClass(sidebarClass);
            if ($(targetContainer).hasClass('page-sidebar-fixed')) {
                generateSlimScroll($('#sidebar [data-scrollbar="true"]'));
            }
        } else {
            $(targetContainer).addClass(sidebarClass);
            if ($(targetContainer).hasClass('page-sidebar-fixed')) {
                $('#sidebar [data-scrollbar="true"]').slimScroll({destroy: true});
                $('#sidebar [data-scrollbar="true"]').removeAttr('style');
            }
            // firefox bugfix
            $('#sidebar [data-scrollbar=true]').trigger('mouseover');
        }
        $(window).trigger('resize');
    });
};


/* 05. Handle Page Load - Fade in
------------------------------------------------ */
var handlePageContentView = function() {
  "use strict";
  $(window).load(function() {
      $.when($('#page-loader').addClass('hide')).done(function() {
        $('#page-container').addClass('in');
      });
  });
};


/* 06. Handle Panel - Remove / Reload / Collapse / Expand
------------------------------------------------ */
var handlePanelAction = function() {
    "use strict";
    
    // remove
    $('[data-click=panel-remove]').hover(function() {
        $(this).tooltip({
            title: 'Remove',
            placement: 'bottom',
            trigger: 'hover',
            container: 'body'
        });
        $(this).tooltip('show');
    });
    $('[data-click=panel-remove]').click(function(e) {
        e.preventDefault();
        $(this).tooltip('destroy');
        $(this).closest('.panel').remove();
    });
    
    // collapse
    $('[data-click=panel-collapse]').hover(function() {
        $(this).tooltip({
            title: 'Collapse / Expand',
            placement: 'bottom',
            trigger: 'hover',
            container: 'body'
        });
        $(this).tooltip('show');
    });
    $('[data-click=panel-collapse]').click(function(e) {
        e.preventDefault();
        $(this).closest('.panel').find('.panel-body').slideToggle();
    });
    
    // reload
    $('[data-click=panel-reload]').hover(function() {
        $(this).tooltip({
            title: 'Reload',
            placement: 'bottom',
            trigger: 'hover',
            container: 'body'
        });
        $(this).tooltip('show');
    });
    $('[data-click=panel-reload]').click(function(e) {
        e.preventDefault();
        var target = $(this).closest('.panel');
        if (!$(target).hasClass('panel-loading')) {
            var targetBody = $(target).find('.panel-body');
            var spinnerHtml = '<div class="panel-loader"><span class="spinner-small"></span></div>';
            $(target).addClass('panel-loading');
            $(targetBody).prepend(spinnerHtml);
            setTimeout(function() {
                $(target).removeClass('panel-loading');
                $(target).find('.panel-loader').remove();
            }, 2000);
        }
    });
    
    // expand
    $('[data-click=panel-expand]').hover(function() {
        $(this).tooltip({
            title: 'Expand / Compress',
            placement: 'bottom',
            trigger: 'hover',
            container: 'body'
        });
        $(this).tooltip('show');
    });
    $('[data-click=panel-expand]').click(function(e) {
        e.preventDefault();
        var target = $(this).closest('.panel');
    
        if ($('body').hasClass('panel-expand') && $(target).hasClass('panel-expand')) {
            $('body, .panel').removeClass('panel-expand');
            $('.panel').removeAttr('style');
            $('[class*=col]').sortable('enable');
        } else {
            $('body').addClass('panel-expand');
            $(this).closest('.panel').addClass('panel-expand');
            $('[class*=col]').sortable('disable');
        }
        $(window).trigger('resize');
    });
};


/* 07. Handle Panel - Draggable
------------------------------------------------ */
var handleDraggablePanel = function() {
  "use strict";
  var target = '[class*=col]';
  var targetHandle = '.panel-heading';
  var connectedTarget = '.row > [class*=col]';
  
  $(target).sortable({
    handle: targetHandle,
    connectWith: connectedTarget
  });
};


/* 08. Handle Tooltip & Popover Activation
------------------------------------------------ */
var handelTooltipPopoverActivation = function() {
  "use strict";
  $('[data-toggle=tooltip]').tooltip();
  $('[data-toggle=popover]').popover();
};


/* 09. Handle Scroll to Top Button Activation
------------------------------------------------ */
var handleScrollToTopButton = function() {
  "use strict";
  $(document).scroll( function() {
    var totalScroll = $(document).scrollTop();
    
    if (totalScroll >= 200) {
      $('[data-click=scroll-top]').addClass('in');
    } else {
      $('[data-click=scroll-top]').removeClass('in');
    }
  });
  
  $('[data-click=scroll-top]').click(function(e) {
    e.preventDefault();
    $('html, body').animate({
      scrollTop: $("body").offset().top
    }, 500);
  });
};


/* 10. Handle Theme & Page Structure Configuration - added in V1.2
------------------------------------------------ */
var handleThemePageStructureControl = function() {
    // COOKIE - Theme File Setting
    if ($.cookie && $.cookie('theme')) {
        if ($('.theme-list').length !== 0) {
            $('.theme-list [data-theme]').closest('li').removeClass('active');
            $('.theme-list [data-theme="'+ $.cookie('theme') +'"]').closest('li').addClass('active');
        }
        var cssFileSrc = 'assets/css/theme/' + $.cookie('theme') + '.css';
        $('#theme').attr('href', cssFileSrc);
    }
    
    // COOKIE - Sidebar Styling Setting
    if ($.cookie && $.cookie('sidebar-styling')) {
        if ($('.sidebar').length !== 0 && $.cookie('sidebar-styling') == 'grid') {
            $('.sidebar').addClass('sidebar-grid');
            $('[name=sidebar-styling] option[value="2"]').prop('selected', true);
        }
    }
    
    // COOKIE - Header Setting
    if ($.cookie && $.cookie('header-styling')) {
        if ($('.header').length !== 0 && $.cookie('header-styling') == 'navbar-inverse') {
            $('.header').addClass('navbar-inverse');
            $('[name=header-styling] option[value="2"]').prop('selected', true);
        }
    }
    
    // THEME - theme selection
    $('.theme-list [data-theme]').live('click', function() {
        var cssFileSrc = 'assets/css/theme/' + $(this).attr('data-theme') + '.css';
        $('#theme').attr('href', cssFileSrc);
        $('.theme-list [data-theme]').not(this).closest('li').removeClass('active');
        $(this).closest('li').addClass('active');
        $.cookie('theme', $(this).attr('data-theme'));
    });
    
    // HEADER - inverse or default
    $('.theme-panel [name=header-styling]').live('change', function() {
        var targetClassAdd = ($(this).val() == 1) ? 'navbar-default' : 'navbar-inverse';
        var targetClassRemove = ($(this).val() == 1) ? 'navbar-inverse' : 'navbar-default';
        $('#header').removeClass(targetClassRemove).addClass(targetClassAdd);
        $.cookie('header-styling',targetClassAdd);
    });
    
    // SIDEBAR - grid or default
    $('.theme-panel [name=sidebar-styling]').live('change', function() {
        if ($(this).val() == 2) {
            $('#sidebar').addClass('sidebar-grid');
            $.cookie('sidebar-styling', 'grid');
        } else {
            $('#sidebar').removeClass('sidebar-grid');
            $.cookie('sidebar-styling', 'default');
        }
    });
    
    // SIDEBAR - fixed or default
    $('.theme-panel [name=sidebar-fixed]').live('change', function() {
        if ($(this).val() == 1) {
            if ($('.theme-panel [name=header-fixed]').val() == 2) {
                alert('Default Header with Fixed Sidebar option is not supported. Proceed with Fixed Header with Fixed Sidebar.');
                $('.theme-panel [name=header-fixed] option[value="1"]').prop('selected', true);
                $('#header').addClass('navbar-fixed-top');
                $('#page-container').addClass('page-header-fixed');
            }
            $('#page-container').addClass('page-sidebar-fixed');
            if (!$('#page-container').hasClass('page-sidebar-minified')) {
                generateSlimScroll($('.sidebar [data-scrollbar="true"]'));
            }
        } else {
            $('#page-container').removeClass('page-sidebar-fixed');
            if ($('.sidebar .slimScrollDiv').length !== 0) {
                $('.sidebar [data-scrollbar="true"]').slimScroll({destroy: true});
                $('.sidebar [data-scrollbar="true"]').removeAttr('style');
            }
            if ($('#page-container .sidebar-bg').length === 0) {
                $('#page-container').append('<div class="sidebar-bg"></div>');
            }
        }
    });
    
    // HEADER - fixed or default
    $('.theme-panel [name=header-fixed]').live('change', function() {
        if ($(this).val() == 1) {
            $('#header').addClass('navbar-fixed-top');
            $('#page-container').addClass('page-header-fixed');
            $.cookie('header-fixed', true);
        } else {
            if ($('.theme-panel [name=sidebar-fixed]').val() == 1) {
                alert('Default Header with Fixed Sidebar option is not supported. Proceed with Default Header with Default Sidebar.');
                $('.theme-panel [name=sidebar-fixed] option[value="2"]').prop('selected', true);
                $('#page-container').removeClass('page-sidebar-fixed');
                if ($('#page-container .sidebar-bg').length === 0) {
                    $('#page-container').append('<div class="sidebar-bg"></div>');
                }
            }
            $('#header').removeClass('navbar-fixed-top');
            $('#page-container').removeClass('page-header-fixed');
            $.cookie('header-fixed', false);
        }
    });
};


/* 11. Handle Theme Panel Expand - added in V1.2
------------------------------------------------ */
var handleThemePanelExpand = function() {
    $('[data-click="theme-panel-expand"]').live('click', function() {
        var targetContainer = '.theme-panel';
        var targetClass = 'active';
        if ($(targetContainer).hasClass(targetClass)) {
            $(targetContainer).removeClass(targetClass);
        } else {
            $(targetContainer).addClass(targetClass);
        }
    });
};


/* 12. Handle After Page Load Add Class Function - added in V1.2
------------------------------------------------ */
var handleAfterPageLoadAddClass = function() {
    if ($('[data-pageload-addclass]').length !== 0) {
        $(window).load(function() {
            $('[data-pageload-addclass]').each(function() {
                var targetClass = $(this).attr('data-pageload-addclass');
                $(this).addClass(targetClass);
            });
        });
    }
};


/* Application Controller
------------------------------------------------ */
var App = function () {
	"use strict";
	
	return {
		//main function
		init: function () {
		
			// slimscroll
			handleSlimScroll();
			
			// sidebar
			handleSidebarMenu();
			handleMobileSidebarToggle();
			handleSidebarMinify();
			
			// theme configuration
			handleThemePageStructureControl();
			handleThemePanelExpand();
			
			handleAfterPageLoadAddClass();
			
			handlePanelAction();
			handleDraggablePanel();
			handelTooltipPopoverActivation();
			handleScrollToTopButton();
			handlePageContentView();
		}
  };
}();