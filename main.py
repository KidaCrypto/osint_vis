import pandas as pd

wallet_array = ["TBfJfBYSpVPLDoFzvg3zCnc4Kvpb48cME5",
"TC7VZ9F3v34byjjdLN9t9c3juzfBisPE4u",
"TD7j5eNShnrSsGb3of8vpe1XXfUNrheeFh",
"TDX3tFFdWFwhBP7Cf5gJRpADpUNxQsys6m",
"TEtJTCuFEzY6jjVNzFtbWGMfrHzfE2aGKU",
"TETZBHSy22wSaufVE1GhNBiDdTYGBJ6aZk",
"TGBYT9Kfs7Za2yWf2TCka5kZq942tKPUAq",
"TGfH7imvH9h6yxusNNPkkwrDzKCg7kFDTf",
"TGS7VL1sHwGnufrQA42GhqHntwcyfNfdt3",
"THB6eY4f85GUab3hdXHhNb53AX1vRzJ83s",
"THL7VtZrHia3fm4UqycAUC8JwodjSqBVxx",
"THNdB4SiwNGibexaigr4YYTZzFRXZGAAox",
"THPopY1MtT3Hsd7YRN8JHNpZDWUAqDQBYm",
"TJAcz547H7FTGCQrgkbtHib5h8f5gR2kuc",
"TJnYxvBHyoZT9GsGGaHzeQxvrGz743k1gq",
"TJqh7J9MnPMSG6cotxBYUsNdQ6eufk8W32",
"TLmB5EYj3Uy1TBgipSSkNiTkp5HVe7qveS",
"TM8PjCzv71EakELjVHoqsZY2aRHoPU8nr5",
"TMJRvUAwpdw67vNuQFH15q34zK3myPgFRy",
"TMYPgVHM61QdY73ttgEKstbSR3vqoXEcZ9",
"TN5fXzNhGW3vCUijECnXgiXhChqLJA4Da4",
"TPAcMFqkaVufH3wNso1Jdvm8HzUnK46PWM",
"TPCQLRv6Bepnd5oPhXtrs1iHpSLchuHAso",
"TPxCncCWLUtRm2ga6NMrPKfumKuQ3zoWXR",
"TQimtt6MmASiLDEsKsfDDaDq5CFRE2BY1F",
"TR2nTb64cQMx6tqFwisoC6o7barFWHhPiw",
"TRAvfmzQNsBAeGaDP9gr5qecGMDqWMo5zn",
"TRkrud54UMLhidM3SdwbEeneTyi42UEcUP",
"TRWpS2JarmZShhQLTfHafnzkQdNKUh1ozK",
"TT7Fes7ErX3JvE71snmbo8PkE8R4NZpMYe",
"TT9z1K9NT3XmMmvC1CaH3U76GFYi3FS1Zt",
"TTnsCooyH7udWbwbybr82BVWEudyHvKvHb",
"TU7N89rqSzYdTpj7tkq98zhmheT9tU1uzY",
"TUig7bV2axB8LvbMqEXauPAuhMFQnTLhZW",
"TUWR8ZhFrCeNg6NX9TDkHspGAgZX56E8Dk",
"TVCtcB4BM8n756v7BHB22kqnP6mHyq8VBN",
"TVXy9j3MHePgN3ydyr3D8NojB5RLD3AcRs",
"TXdNFmv2wngkc9WT4sT9HdFgVWbYyfX21L",
"TXPggkiHzYZofVqpzMDS19ePG6qmcnu3gq",
"TXQyMhsxZfcGqPdi1TAYWJ5bVkcVyR2ye9",
"TXRBsytHfJDoAKRdcedgLsoHudh1xJGUdC",
"TXs56ZWCpZ7yBBhDZ8J8tFqc9y31Ra9RHC",
"TZ1bLdAGQPH9cQkR372TGZJ99fjBi1juTQ",
"TRwvSmistRy7vK8mq2xpPA85fj9wRJKcUB",
"TKcPMYyy2BkVCUEoLgh22KnhzYPuYJt7hv",
"TDnytyeHuRrpQ2wbpDot8io92bHs78XrMv",
"TQn9oh6Mw6jLfgzh23AVHsCcfC9ZE41fne",
"TCWMveoWyAwkCthHC43nfgbtmAfPGXYhQD",
"TDAegnxRRBVuRFJ1tkpmignshcu12nfoQF",
"TFS7HvL8Y7zWoSR6FroD9SGiKCpWTZLLLX",
"TGSv6fGeiZbWA1jBdsgkGLumtqp4wFXxzq",
"THBPKbkuVSxNG7cq8bAvicrTm2YpMMZVKQ",
"TJZnMKRAXWqhewxDUGvsfaoe8exUjHPwA6",
"TM45NsDQ1YUMMHosa2uK5FZbxxggNzxSys",
"TMmEYcSL4KhzJuYpRH16aLsG16YoFyYKUq",
"TNT8WTuCoPwuYzScrHwbv5Wzw9XBwu9u3q",
"TPpRxpTw3Mn71rHzStQfjHB369zxHYqQiz",
"TQ4HeWsnzXexz2UKY3Ef94xg3rnWkawirR",
"TQLoZxoAu2arL3jCyz5ToZf4gqkmvXxtTy",
"TSgiPLeKKTd6vQa2aLfb1QFmNV9DW52xYK",
"TU3bxJ7FRpwsfwwc7bQLa9Jr89e7UzWB3m",
"TUtw7GQJssJ6WtBE1J2xKks7VimKP8m587",
"TVzsknku8cubpukTmUVn5Ro747Bgw3GS63",
"TXBMWt3T4WhFkcPnob1567cGDM3ou27GWE",
"TXXfxvnjg4497duutm5uEHUgqAhSVoM4nS",
"TCG5LT8GZu9xedHbfwo2Mea2nJJbi5QGTv",
"THsPCpqBmmi8CzMWvQ1Zw7cMZaJ77hnmVW",
"TK8qQuPSCeQx6AKuqHLX4xycSVFNXGVWQy",
"TTxuaC7zJ5QbBhnUL2KEkQbFc5UEipE1fd",
"TVoJZwG6SZrpk2Y11w2WW54HyvJmKTkeqG",
"TWvsfLNZrB8xPEeUE5Jzo94MzNYcCZ3ia8",
"TY3TUu4RwSDmUqQAbQ66vU3tRdkqPC19M4",
"TY825nrM5GiztWFRQW3JpPUAGuZhWPisSA"
]

pij_wallets = [
"TY825nrM5GiztWFRQW3JpPUAGuZhWPisSA",
"TY3TUu4RwSDmUqQAbQ66vU3tRdkqPC19M4",
"TWvsfLNZrB8xPEeUE5Jzo94MzNYcCZ3ia8",
"TVoJZwG6SZrpk2Y11w2WW54HyvJmKTkeqG",
"TTxuaC7zJ5QbBhnUL2KEkQbFc5UEipE1fd",
"TK8qQuPSCeQx6AKuqHLX4xycSVFNXGVWQy",
"THsPCpqBmmi8CzMWvQ1Zw7cMZaJ77hnmVW",
"TCG5LT8GZu9xedHbfwo2Mea2nJJbi5QGTv",
"TXXfxvnjg4497duutm5uEHUgqAhSVoM4nS",
"TXBMWt3T4WhFkcPnob1567cGDM3ou27GWE",
"TVzsknku8cubpukTmUVn5Ro747Bgw3GS63",
"TUtw7GQJssJ6WtBE1J2xKks7VimKP8m587",
"TU3bxJ7FRpwsfwwc7bQLa9Jr89e7UzWB3m",
"TSgiPLeKKTd6vQa2aLfb1QFmNV9DW52xYK",
"TQLoZxoAu2arL3jCyz5ToZf4gqkmvXxtTy",
"TQ4HeWsnzXexz2UKY3Ef94xg3rnWkawirR",
"TPpRxpTw3Mn71rHzStQfjHB369zxHYqQiz",
"TNT8WTuCoPwuYzScrHwbv5Wzw9XBwu9u3q",
"TMmEYcSL4KhzJuYpRH16aLsG16YoFyYKUq",
"TM45NsDQ1YUMMHosa2uK5FZbxxggNzxSys",
"TJZnMKRAXWqhewxDUGvsfaoe8exUjHPwA6",
"THBPKbkuVSxNG7cq8bAvicrTm2YpMMZVKQ",
"TGSv6fGeiZbWA1jBdsgkGLumtqp4wFXxzq",
"TFS7HvL8Y7zWoSR6FroD9SGiKCpWTZLLLX",
"TDAegnxRRBVuRFJ1tkpmignshcu12nfoQF",
"TCWMveoWyAwkCthHC43nfgbtmAfPGXYhQD"
]
df = pd.read_csv('./ant/trc20_txs.csv')

df['hour'] = pd.to_datetime(df['block_timestamp'] * 1000, unit='us').dt.strftime('%H')
df['month'] = pd.to_datetime(df['block_timestamp'] * 1000, unit='us').dt.strftime('%Y-%m')
df['date'] = pd.to_datetime(df['block_timestamp'] * 1000, unit='us').dt.strftime('%Y-%m-%d')
df = df[df['token_info.symbol'] == 'USDT']
df['value'] = df['value'].apply(lambda x: int(x)) / pow(10, df['token_info.decimals'])

receiving_df = df[df['to'].isin(wallet_array)]
with open("output/receiving_df.json", "w") as outfile:
    receiving_df.reset_index(inplace=True)
    outfile.write(receiving_df.to_json(orient="values"))

senders = receiving_df[~receiving_df['from'].isin(wallet_array)]['from'].unique()
with open("output/senders.json", "w") as outfile:
    outfile.write(pd.Series(senders).to_json(orient="values"))

outgoing_df = df[df['from'].isin(wallet_array)]
with open("output/outgoing_df.json", "w") as outfile:
    outgoing_df.reset_index(inplace=True)
    outfile.write(outgoing_df.to_json(orient="values"))
    
inter_df = receiving_df[receiving_df['from'].isin(wallet_array)]
with open("output/inter_df.json", "w") as outfile:
    inter_df.reset_index(inplace=True)
    outfile.write(inter_df.to_json(orient="values"))

return_to_sender = outgoing_df[outgoing_df['to'].isin(senders)]
with open("output/return_to_sender_df.json", "w") as outfile:
    return_to_sender.reset_index(inplace=True)
    outfile.write(return_to_sender.to_json(orient="values"))

# overall
all_by_date = receiving_df[['month', 'value']].groupby('month').sum()
all_by_date['tx_count'] = receiving_df[['month']].groupby('month')['month'].count()
with open("output/all_by_date.json", "w") as outfile:
    all_by_date.reset_index(inplace=True)
    outfile.write(all_by_date.to_json(orient="values"))

all_return =  df[df['from'].isin(wallet_array)]
all_return =  all_return[all_return['to'].isin(senders)]
all_inter =  df[df['from'].isin(wallet_array)]
all_inter =  all_inter[all_inter['to'].isin(wallet_array)]

all_receives_by_date = receiving_df[['month', 'value']].groupby('month').sum()
all_returns_by_date = all_return[['month', 'value']].groupby('month').sum()
all_inter_by_date = all_inter[['month', 'value']].groupby('month').sum()

all_agg = all_receives_by_date.join(all_returns_by_date, lsuffix='_receive', rsuffix='_return').fillna(0)
all_agg = all_agg.join(all_inter_by_date, rsuffix='_inter').fillna(0)
all_agg['net'] = all_agg['value_receive'] - all_agg['value_return'] - all_agg['value']
all_agg['tx_count'] = receiving_df[['month']].groupby('month')['month'].count()
all_agg['return_tx_count'] = all_return[['month']].groupby('month')['month'].count()
all_agg['inter_tx_count'] = all_inter[['month']].groupby('month')['month'].count()
all_agg.fillna(0, inplace=True)
with open("output/all_net.json", "w") as outfile:
    all_agg.reset_index(inplace=True)
    outfile.write(all_agg.to_json(orient="values"))

print('Inter Addresses Transfer Values: ' + str(inter_df['value'].sum()))
print('Receiving Values: ' +  str(receiving_df['value'].sum()))
print('Outgoing Values: ' +  str(outgoing_df['value'].sum()))
print('Returned Values: ' +  str(return_to_sender['value'].sum()))

# PIJ
pij_receives = df[df['to'].isin(pij_wallets)]
with open("output/pij_receives.json", "w") as outfile:
    pij_receives_adj = pij_receives[pij_receives['month'] == '2021-09']
    outfile.write(pij_receives_adj.to_json(orient="values"))

pij_by_date = pij_receives[['month', 'value']].groupby('month').sum()
pij_by_date['tx_count'] = pij_receives[['month']].groupby('month')['month'].count()
with open("output/pij_by_date.json", "w") as outfile:
    pij_by_date.reset_index(inplace=True)
    outfile.write(pij_by_date.to_json(orient="values"))

pij_return =  df[df['from'].isin(pij_wallets)]
pij_return =  pij_return[pij_return['to'].isin(senders)]
pij_inter =  df[df['from'].isin(pij_wallets)]
pij_inter =  pij_inter[pij_inter['to'].isin(pij_wallets)]

pij_receives_by_date = pij_receives[['month', 'value']].groupby('month').sum()
pij_returns_by_date = pij_return[['month', 'value']].groupby('month').sum()
pij_inter_by_date = pij_inter[['month', 'value']].groupby('month').sum()

pij_agg = pij_receives_by_date.join(pij_returns_by_date, lsuffix='_receive', rsuffix='_return').fillna(0)
pij_agg = pij_agg.join(pij_inter_by_date, rsuffix='_inter').fillna(0)
pij_agg['net'] = pij_agg['value_receive'] - pij_agg['value_return'] - pij_agg['value']
pij_agg['tx_count'] = pij_receives[['month']].groupby('month')['month'].count()
pij_agg['return_tx_count'] = pij_return[['month']].groupby('month')['month'].count()
pij_agg['inter_tx_count'] = pij_inter[['month']].groupby('month')['month'].count()
pij_agg.fillna(0, inplace=True)
with open("output/pij_net.json", "w") as outfile:
    pij_agg.reset_index(inplace=True)
    outfile.write(pij_agg.to_json(orient="values"))

print('PIJ Net Received: ' +  str(pij_agg['net'].sum()))

# get actual received only
receiving_df = receiving_df[~receiving_df['from'].isin(wallet_array)]

hour_df = receiving_df[['hour', 'from']]
sender_hour_df_agg = hour_df.groupby('hour').nunique()
hour_df = receiving_df[['hour', 'value']]
value_hour_df_agg = hour_df.groupby('hour').sum()

hour_df_agg = sender_hour_df_agg.join(value_hour_df_agg)

with open("output/hour_total_value.json", "w") as outfile:
    hour_df_agg.reset_index(inplace=True)
    outfile.write(hour_df_agg.to_json(orient="values"))