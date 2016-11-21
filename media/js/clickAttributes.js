
app.clickAttributes = (function() {

	var getSurveyAttributes = function(data, activity) {
		attrs = [];
		if (activity !== 'All Activities') {
			for (var key in data) {
			  	if (data.hasOwnProperty(key) && data[key]) {
			  		if (key === activity) {
			  			if (data[key] === 1) {
			    			attrs.push({'display': key, 'data': data[key] + ' day'});
			  			} else {
			    			attrs.push({'display': key, 'data': data[key] + ' days'});
			  			}
			  		}
			  	}
			}
			attrs.push({'display': 'Total Activity Days (All Activities)', 'data': data['Total Activity Days']});
            // attrs.push({'display': 'UniqueID', 'data': data['UniqueID']});
		} else {
			// for (var key in data) {
			//   	if (data.hasOwnProperty(key) && data[key]) {
			//   		if (key !== 'Total Activity Days' && key !== 'Other' && key !== 'UniqueID') {
			//   			if (data[key] === 1) {
			//     			attrs.push({'display': key, 'data': data[key] + ' day'});
			//   			} else {
			//     			attrs.push({'display': key, 'data': data[key] + ' days'});
			//   			}
			//   		}
			//   	}
			// }
			// // alphabetize and then put Total at top (or bottom)
			// attrs = _.sortBy(attrs, function(obj){ return obj['display']; });
			// if (data['Other']) {
			// 	if (data['Other'] === 1) {
			// 		attrs.push({'display': 'Other', 'data': data['Other'] + ' day'});
			// 	} else {
			// 		attrs.push({'display': 'Other', 'data': data['Other'] + ' days'});
			// 	}
			// }
			attrs.unshift({'display': 'Total Activity Days (All Activities)', 'data': data['Total Activity Days']});
            // attrs.push({'display': 'UniqueID', 'data': data['UniqueID']});
		}
		return attrs;
	};

	  var toSquareMiles = function(sqmeters) {
			sqmiles = Math.round(parseFloat(sqmeters)/2590000.0);
			return sqmiles.toLocaleString() + ' mi&sup2;'

		};

    // Called from utfGridClickHandling in map.js (for Planning Grid click handling)
    var getGridAttributes = function (data) {
        attrs = [];

        if ('NAME' in data) {
            attrs.push({'display': 'Name', 'data': data['NAME'].toLocaleString()});
        }

				if ('AREA_NAME' in data) {
            attrs.push({'display': 'Name', 'data': data['AREA_NAME'].toLocaleString()});
        }

				if ('Name' in data) {
            attrs.push({'display': 'Name', 'data': data['Name'].toLocaleString()});
        }

        if ('SiteName' in data) {
            attrs.push({'display': 'Name', 'data': data['SiteName'].toLocaleString()});
        }

        if ('ID' in data) {
            attrs.push({'display': 'Id', 'data': data['ID'].toLocaleString()});
        }
        // if ('GRIDCODE' in data) {
        //     attrs.push({'display': 'Gridcode', 'data': data['GRIDCODE'].toLocaleString()});
        // }

        // Area of mapped Dense Acropora cervicornis patches in m²
        if ('mean_fthm' in data) {
            attrs.push({'display': 'Mean depth', 'data': data['mean_fthm'].toLocaleString() + ' fathoms'});
        }
        // Whether a cell intersects witha designated anchorage
        if ('hsall1_m2' in data) {
            attrs.push({'display': 'Predicted habitat suitability (class 1) for all 6 relevant taxa of deep-sea coral', 'data': toSquareMiles(data['hsall1_m2'])});
        }
        if ('hsall2_m2' in data) {
            attrs.push({'display': 'Predicted habitat suitability (class 2) for all 6 relevant taxa of deep-sea coral', 'data': toSquareMiles(data['hsall2_m2'])});
        }
        if ('hsall3_m2' in data) {
            attrs.push({'display': 'Predicted habitat suitability (class 3) for all 6 relevant taxa of deep-sea coral', 'data': toSquareMiles(data['hsall3_m2'])});
        }
        if ('hsall4_m2' in data) {
            attrs.push({'display': 'Predicted habitat suitability (class 4) for all 6 relevant taxa of deep-sea coral', 'data': toSquareMiles(data['hsall4_m2'])});
        }

        if ('hpc_est_m2' in data) {
            attrs.push({'display': 'Estuary habitat of particular concern', 'data': toSquareMiles(data['hpc_est_m2'])});
        }
        if ('hpc_klp_m2' in data) {
            attrs.push({'display': 'Kelp habitat of particular concern', 'data': toSquareMiles(data['hpc_klp_m2'])});
        }
        if ('hpc_rck_m2' in data) {
            attrs.push({'display': 'Rocky reef habitat of particular concern', 'data': toSquareMiles(data['hpc_rck_m2'])});
        }
        if ('hpc_sgr_m2' in data) {
            attrs.push({'display': 'Seagrass habitat of particular concern', 'data': toSquareMiles(data['hpc_sgr_m2'])});
        }

        if ('sft_sub_m2' in data) {
            attrs.push({'display': 'Soft Substrate', 'data': toSquareMiles(data['sft_sub_m2'])});
        }
        if ('mix_sub_m2' in data) {
            attrs.push({'display': 'Mixed Substrate', 'data': toSquareMiles(data['mix_sub_m2'])});
        }
        if ('hrd_sub_m2' in data) {
            attrs.push({'display': 'Hard Substrate', 'data': toSquareMiles(data['hrd_sub_m2'])});
        }
        if ('rck_sub_m2' in data) {
            attrs.push({'display': 'Inferred Rock Substrate', 'data': toSquareMiles(data['rck_sub_m2'])});
        }
        if ('cnt_cs' in data) {
            attrs.push({'display': 'Coral (excluding pennatulids) and sponge presence', 'data': data['cnt_cs'].toLocaleString()});
        }
        if ('cnt_penn' in data) {
            attrs.push({'display': 'Pennatulid (sea pen/sea whip) presence', 'data': data['cnt_penn'].toLocaleString()});
        }

        if ('Area_m2' in data) {
            attrs.push({'display': 'Area', 'data': toSquareMiles(data['Area_m2'])});
        }

        if ('Shape_Area' in data) {
            attrs.push({'display': 'Area', 'data': toSquareMiles(data['Shape_Area'])});
        }

				if ('AreaMi2' in data) {
						attrs.push({'display': 'Area', 'data': data['AreaMi2'].toLocaleString() + ' mi&sup2;'});
				}

				if ('GRIDCODE' in data) {
					attrs.push({'display':'Class', 'data': data['GRIDCODE']})
				}

        if ('LoHS' in data) {
            attrs.push({'display': 'Suitability', 'data': data['LoHS'].toLocaleString()});
        }


        // // Depth Range
        // if ('MaxDpth_ft' in data && 'MinDpth_ft' in data) {
        //     attrs.push({'display': 'Depth Range', 'data': data['MinDpth_ft'] + ' to ' + data['MaxDpth_ft'] + ' feet'});
        // }
        // // Average Depth
        // if ('MeanDpth_f' in data) {
        //     attrs.push({'display': 'Average Depth', 'data': data['MeanDpth_f']});
        // }

        // A number assigned to each cell that is unique to the dataset. (no duplicates)
        if ('UniqueID' in data) {
            attrs.push({'display': 'UniqueID (for testing)', 'data': data['UniqueID']});
        }

        if ('COM_allow' in data) {
            var com_allow = ((data['COM_allow'] == 'no') ? 'Prohibited' : 'Allowed') ;
            attrs.push({'display': 'Commercial Fishing', 'data': com_allow});
        }

        if ('CPFV_allow' in data) {
            var cpfv_allow = ((data['CPFV_allow'] == 'no') ? 'Prohibited' : 'Allowed') ;
            attrs.push({'display': 'Charter Fishing', 'data': cpfv_allow});
        }

				if ('PROHIBIT' in data) {
						attrs.push({'display':'Prohibits', 'data': data['PROHIBIT']});
				}

				if ('STATE' in data) {
						attrs.push({'display':'State', 'data': data['STATE']});
				}

				if ('State' in data) {
						attrs.push({'display':'State', 'data': data['State']});
				}

				if ('rationale' in data) {
						var rationale = data['rationale'];
						if (rationale == 'Reopen') {
							rationale = 'Reopening';
						}
						attrs.push({'display':'Type', 'data': rationale});
				}

        if ('RegAction' in data) {
            attrs.push({'display': 'Type', 'data': data['RegAction'].toLocaleString()});
        }

				if ('EFH_prop' in data) {
						attrs.push({'display': 'Description', 'data': data['EFH_prop']});
				}

				if ('SC_NAME' in data) {
						attrs.push({'display': 'Type', 'data': data['SC_NAME']});
				}

				if ('DESCRIPTIO' in data && data['DESCRIPTIO'] != '') {
						attrs.push({'display': 'Notes', 'data': data['DESCRIPTIO']});
				}

        if ('Proposer' in data) {
            attrs.push({'display': 'Proposer', 'data': data['Proposer'].toLocaleString()});
        }

        return attrs;
    };

    return {
    	getGridAttributes: getGridAttributes,
    	getSurveyAttributes: getSurveyAttributes
    };

})();
