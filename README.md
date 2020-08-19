<div style="border-bottom:none;">
  <div align="center"> 
    <img style="border-bottom:none;" src="https://www.mad.tf.fau.de/files/2019/04/logo_mad.png">
    <h1>Increasing stability for GAN training using past exploration</h1>
  </div>
</div>

## Motivation
Applications in the context of industry suffer always from the same curse: "Too little, too similar data". Research suggests, that Generative Adversarial Networks are a possibility to generate new (non-exisiting) data samples by using an existing data distribution. However, there exist several challanges to actually model this distribution in a stable and discriminative way. The hypothesis states, that the discriminator in a GAN only models based on the current generator and forgets all past explorations. This would mean, the performance of a discrimnator (and therfore the generator) can be improved by sampling over all past explorations of the GAN in a correct manner. This project explores this exact possibility.

## Content

- Code as [iPython](https://mad-srv.informatik.uni-erlangen.de/MadLab/industry-4.0/seminar-i4.0/ss2020/increasing-stability-for-gan-training-using-past-exploration/-/tree/master/Code/Notebooks) 
- Project report as [PDF](https://mad-srv.informatik.uni-erlangen.de/MadLab/industry-4.0/seminar-i4.0/ss2020/increasing-stability-for-gan-training-using-past-exploration/-/tree/master/Paper)
- Project presentation as [PDF](https://mad-srv.informatik.uni-erlangen.de/MadLab/industry-4.0/seminar-i4.0/ss2020/increasing-stability-for-gan-training-using-past-exploration/-/tree/master/Paper)

## How do I get the code?

You should know that.

## How do I get the data?

Unfortunately, the data is not provided on a public host. So, please do it the old fashioned way and write an [email](timo.bohnstedt@gmail.com), so that we can find a way.

## What else do I need to run the code?

```
conda env create -f environment.yml
conda activate mad40-env
```

### How can I Run the Notebook/ Source?

You should know that as well :P

## Deployment

Just pull the repo, if you wanna change sth you can ask :)

Please do NOT commit any data files into the repositories. Data should always be kept seperate from code!

## Authors

* **Timo Bohnstedt** - *Coding, Report* - [GitHub Bohniti](https://github.com/bohniti)

## License

Pretty much the BSD license, just don't repackage it and call it your own please!
Also if you do make some changes, feel free to make a pull request and help make things more awesome!

## Acknowledgments

The author would like to thank his Franz Koeferl and the MADI40-Team from the Machine Learning & Data Analytics Lab for excellent support. 