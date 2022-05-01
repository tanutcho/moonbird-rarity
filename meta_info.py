import streamlit as st
import pandas as pd
import numpy as np

@st.cache(suppress_st_warning=True)
def get_moonbird_info():
    moonbird_metainfo = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/978157dd-d6b3-45cb-bc75-9fb68cb7f3b1/data/latest')
    return moonbird_metainfo

moonbird_metainfo = get_moonbird_info()

meta_json = pd.json_normalize(moonbird_metainfo['TOKEN_METADATA']).fillna('None')
bg_prob = dict(meta_json.background.value_counts()/10000)
beak_prob = dict(meta_json.beak.value_counts()/10000)
body_prob = dict(meta_json.body.value_counts()/10000)
eyes_prob = dict(meta_json.eyes.value_counts()/10000)
feathers_prob = dict(meta_json.feathers.value_counts()/10000)
headwear_prob = dict(meta_json.headwear.value_counts()/10000)
outerwear_prob = dict(meta_json.outerwear.value_counts()/10000)
eyewear_prob = dict(meta_json.eyewear.value_counts()/10000)


def get_rarity_score(token_id):
  row_number = moonbird_metainfo.loc[moonbird_metainfo['TOKEN_ID'] == token_id].index.values
  selected = meta_json.loc[row_number]
  # st.write(selected)
  score = (1/bg_prob[selected['background'].values[0]])+(1/beak_prob[selected['beak'].values[0]])+(1/body_prob[selected['body'].values[0]])+(1/eyes_prob[selected['eyes'].values[0]])+(1/feathers_prob[selected['feathers'].values[0]])+(1/headwear_prob[selected['headwear'].values[0]])+(1/outerwear_prob[selected['outerwear'].values[0]])+(1/eyewear_prob[selected['eyewear'].values[0]])
  st.metric('Rarity Score',score)



  st.image(moonbird_metainfo.loc[row_number]['IMAGE_URL'].values[0])
  st.write('Background Prob: ',bg_prob[selected['background'].values[0]])
  st.write('Beak Prob: ',beak_prob[selected['beak'].values[0]])
  st.write('Body Prob: ',body_prob[selected['body'].values[0]])
  st.write('Eyes Prob: ',eyes_prob[selected['eyes'].values[0]])
  st.write('Feathers Prob: ',feathers_prob[selected['feathers'].values[0]])
  st.write('Headwear Prob: ',headwear_prob[selected['headwear'].values[0]])
  st.write('Outerwear Prob: ',outerwear_prob[selected['outerwear'].values[0]])
  st.write('Eyewear Prob: ',eyewear_prob[selected['eyewear'].values[0]])




st.title ('NFT Rarity Scoring')
token_id = st.number_input('Moonbird Token ID')
st.write('Token ID ', token_id)
if st.button('Find Rarity'):
     get_rarity_score(token_id)
else:
     st.write('-')

if st.button('Collection Info'):
    st.json(bg_prob)
    st.json(beak_prob)
    st.json(body_prob)
    st.json(eyes_prob)
    st.json(feathers_prob)
    st.json(headwear_prob)
    st.json(outerwear_prob)
    st.json(eyewear_prob)
else:
     st.write('-')
