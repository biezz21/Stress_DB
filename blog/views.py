from django.shortcuts import render
from .models import Description, tpm_list
from django import forms
import pandas as pd
import numpy as np
from operator import itemgetter, attrgetter

# Create your views here.


def post_list(request):


	treat_list, ix, tpm_values, tpm_set, tpm_set_fix, data = [],[],[],[], [], []

# tissue select -> push treat_list

	tissue = request.GET.get('tissueSelect')

	if str(tissue) == 'None':
		tissue = 'root'
	tissue_selected 	= Description.objects.filter(Tissue=tissue)
	treat_list			= [x.Treat for x in tissue_selected]
	ix					+= [int(x.id) for x in tissue_selected]

	tissue_list = Description.objects.all()
	tissue_list_set = set([x.Tissue for x in tissue_list])


# gene select -> push tpm_output
	query 				= request.GET.get("gene")

	if str(query)		== 'None':
		query 			= 'AT1G01010.1'

	gene_selected 		= tpm_list.objects.filter(target_id=query)
	tpm_values 			+= [x.Tpm for x in gene_selected]
	tpm_set				+= [np.array(x.split(','))[ix] for x in tpm_values]
	tpm_set_fix			+= [list(map(float,x.tolist())) for x in tpm_set]
	tpm_output			=  sum(tpm_set_fix,[])
			
# csv file 
	data				+= [[x,y] for x, y in zip(tpm_output, treat_list)]
	data_sort   		= sorted(data,  key=lambda x: x[1]=='Con', reverse=True)
	DB_output			= [(np.array(data_sort))]
	csv_file			= '/static/output.csv'
			
	np.savetxt('./blog/static/output.csv', np.column_stack((DB_output)), delimiter = ',', fmt = '%s', header = 'tpm,treatment',comments="")

	return_source 		= {'csv_file':csv_file, 'query':query, 'tissue':tissue, 'tissue_list_set':tissue_list_set}

	return render(request, 'blog/post_list.html', return_source)

	