import quandl
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from matplotlib import style
style.use('ggplot')
# style.use('fivethirtyeight')
api_key='_5n_fVMvgJyas1-KUj6M'


def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][4:]


def grab_initial_state_data():
    # states = state_list()

    main_df  = quandl.get('FMAC/HPI', authtoken=api_key)

    # for abbv in states:
    #     query = "FMAC/HPI_"+str(abbv)
    #     print(query)
    #     try:
    #         df = quandl.get('FMAC/HPI', authtoken=api_key)
    #         if main_df.empty:
    #              main_df = df
    #         else:
    #              main_df = main_df.join(df)
    #              print(query)
    #     except Exception:
    #         print("Exception for :" + query)
    #         continue

    pickle_out = open('fiddy_states.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

# grab_initial_state_data()
HPI_data = pd.read_pickle('fiddy_states.pickle')
# print(HPI_data[[1,5,6,7,8,9,10]].head(10))
HPI_data[[1,5,6,7,8,9,10]].plot()
# HPI_data.plot()
# plt.legend().remove()
plt.show()