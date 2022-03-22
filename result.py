def calculate_result(result):
    # print(result)
    #if result['squat']==1.0 and result['ip']:
    #    if result['sd']=='safe' and result['pop'] and result['sdom']=='yes':
    #       return 'Not a Phishing Website'
    #   return 'Not likely to be a phishing website'
    #else:
    #    if result['sd']=='safe' and result['pop'] and result['sdom']=='yes':
    #        return 'Likely to be a phishing website'
    #   return 'A Phishing website'
    if result['squat']>=0.6 and result['ip'] and result['pop']:
        return 'Not A Phishing Website'
    else:
        return 'Likely To Be A Phishing Website'