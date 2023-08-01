contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reportedly sliced.",
            "The slicing process was well presented."]
filenames = ["doc.txt", "report.txt", "presentation.txt"]

for file, content in zip(filenames, contents):
    with open(f"../files/{file}", 'w') as fh:
        fh.writelines(content)