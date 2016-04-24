$.widget( "custom.catcomplete", $.ui.autocomplete, {

     _create: function() {
         this._on(this.element, {
          focus: function(event) {
            this.search();
          },

          click: function(event) {
            this.search();
          },
        });
        this._super();
        this.widget().menu( "option", "items", "> :not(.ui-autocomplete-category)" );
    },

     _renderMenu: function( ul, items ) {

         var that = this,
        currentCategory = "";

         $.each( items, function( index, item ) {
            var li;
            if ( item.category != currentCategory ) {
                ul.append( "<li class='ui-autocomplete-category " + item.category + "'>" + item.category + "</li>" );
                currentCategory = item.category;
            }

            li = that._renderItemData( ul, item );

            if ( item.category ) {
                li.attr( "aria-label", item.category + " : " + item.label );
            }
        });
    },

     _renderItem: function( ul, item ) {
		return $( "<li>" )
		.addClass(item.category)
		.attr( "data-value", item.value )
		.append( $( "<a>" ).text( item.label ) )
		.appendTo( ul );
	}
});
