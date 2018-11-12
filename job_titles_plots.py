def job_titles_plots(file_path = r'C:\Users\DELL\Desktop\Train_rev1.csv'):
    '''
    Reads raw data from an execl file.
    This function create three figures, the frequency of job salary,
    number of terms in job titles and the wordcloud.
        
    
    '''
    assert isinstance(file_path, str)
    
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    from collections import Counter
    from wordcloud import WordCloud # need to be installed first
    
    #figure 1. Frequency of job salary
    data = pd.read_csv(file_path)
    data.SalaryNormalized.hist(figsize = (12,6)); plt.ylabel('frequency'); plt.xlabel(u'salary (£)'); plt.yscale('log')
    
    #figure 2. Number of terms in job titles
    #generate a single str and get rid of 0-9, a-z, A-Z, NaN.......
    text = ' '.join(data['Title'].replace(r'[^0-9a-zA-Z]+',' ',regex=True).fillna('').str.lower())
    stop_words = ['k','c','in','to','it','and','of',''] #redundant words 
    most_common_terms = Counter([w for w in text.split(' ') if w not in stop_words]).most_common(50)

    labels, values = zip(*most_common_terms)
    indexes = np.arange(len(labels))
    width = 0.5
    my_colors = [(0.5,0.4,0.5), (0.75, 0.75, 0.25)] #choose RGB values for different color
    #my_colors = [(x/100.0, x/200.0, 0.75) for x in range(len(indexes))] #gradient color

    plt.figure(figsize=(15,10))
    plt.bar(indexes, values, width,color = my_colors)
    plt.xticks(indexes, labels, rotation='vertical')
    plt.xlabel("Term of Titles");plt.ylabel("Number of terms")
    plt.show()

    #figure 3. Wordcloud    
    wordcloud = WordCloud(max_font_size=40, relative_scaling=0.5,collocations=False).generate(text)
    plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")
    
job_titles_plots()
